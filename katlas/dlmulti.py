# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_DL-multi.ipynb.

# %% auto 0
__all__ = ['seed_everything', 'DualInputDataset', 'MLP', 'CNN1D_1', 'DualInputModel', 'ConvBlock', 'CNN1D_2', 'train_dl_multi',
           'predict_dl']

# %% ../nbs/04_DL-multi.ipynb 3
from fastbook import *
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from scipy.stats import spearmanr,pearsonr
from .core import *
from .feature import *
from sklearn.model_selection import *
from torchsummary import summary
import torch.nn.init as init
from .train import *

# %% ../nbs/04_DL-multi.ipynb 4
def seed_everything(seed=123):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

# %% ../nbs/04_DL-multi.ipynb 7
class DualInputDataset:
    def __init__(self, 
                 df, # a dataframe of values
                 feat_col1, # first set of feature columns
                 feat_col2, # second set of feature columns
                 target_col=None # Will return test set for prediction if target col is None
                ):
        "A dataset designed for dual-input models"
        
        self.test = False if target_col is not None else True
        
        self.X1 = df[feat_col1].values
        self.X2 = df[feat_col2].values
        self.y = df[target_col].values if not self.test else None
        
        self.len = df.shape[0]

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        X1 = torch.Tensor(self.X1[index])
        X2 = torch.Tensor(self.X2[index])
        if self.test:
            return X1, X2
        else:
            y = torch.Tensor(self.y[index])
            return X1, X2, y

# %% ../nbs/04_DL-multi.ipynb 26
class MLP(Module):
    def __init__(self, num_features, hidden_units, dp=0.2):
        layers = []
        input_units = num_features
        for units in hidden_units:
            layers.extend([
                nn.Linear(input_units, units),
                nn.BatchNorm1d(units),
                nn.Dropout(dp),
                nn.PReLU()
            ])
            input_units = units
        self.net = nn.Sequential(*layers)
    
    def forward(self, x):
        return self.net(x)

# %% ../nbs/04_DL-multi.ipynb 32
class CNN1D_1(Module):
    
    def __init__(self, 
                 num_features, # this does not matter, just for format
                ):

        self.conv1 = nn.Conv1d(in_channels=1, out_channels=3, kernel_size=3, dilation=1, padding=1, stride=1)
        self.pool1 = nn.MaxPool1d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv1d(in_channels=3, out_channels=8, kernel_size=3, dilation=1, padding=1, stride=1)
        self.pool2 = nn.MaxPool1d(kernel_size=2, stride=2)
        self.flatten = Flatten()


    def forward(self, x):
        x = x.unsqueeze(1) # need shape (bs, 1, num_features) for CNN
        x = self.pool1(nn.functional.relu(self.conv1(x)))
        x = self.pool2(nn.functional.relu(self.conv2(x)))
        x = self.flatten(x)

        return x

# %% ../nbs/04_DL-multi.ipynb 37
class DualInputModel(nn.Module):
    def __init__(self, model1, model2, concat_dim, num_targets):
        super(DualInputModel, self).__init__()
        
        self.model1 = model1  
        self.model2 = model2
        
        # Final MLP layer after concatenation
        self.fc1 = nn.Linear(in_features = concat_dim, out_features=concat_dim//2)
        self.fc2 = nn.Linear(in_features=concat_dim//2, out_features=num_targets)

    def forward(self, x1, x2):
        x1 = self.model1(x1)
        x2 = self.model2(x2)
        x = torch.cat([x1, x2], dim=1)  # Concatenate along features
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# %% ../nbs/04_DL-multi.ipynb 41
def ConvBlock(in_channels, 
              out_channels, 
              kernel_size, 
              stride, 
              padding, 
              dropout_rate):
    return nn.Sequential(
        nn.BatchNorm1d(in_channels),
        nn.Dropout(dropout_rate),
        nn.utils.weight_norm(nn.Conv1d(in_channels, out_channels, kernel_size, stride, padding)),
        nn.ReLU()
    )

# %% ../nbs/04_DL-multi.ipynb 42
class CNN1D_2(Module):
    
    def __init__(self, 
                 num_features, 
                 num_targets, 
                 hidden_size=4096):

        cha_1 = 256
        cha_2 = 512
        cha_3 = 512

        cha_1_reshape = int(hidden_size/cha_1)
        cha_po_1 = int(hidden_size/cha_1/2)
        cha_po_2 = int(hidden_size/cha_1/2/2) * cha_3

        self.cha_1 = cha_1
        self.cha_2 = cha_2
        self.cha_3 = cha_3
        self.cha_1_reshape = cha_1_reshape
        self.cha_po_1 = cha_po_1
        self.cha_po_2 = cha_po_2

        self.batch_norm1 = nn.BatchNorm1d(num_features)
        self.dropout1 = nn.Dropout(0.1)
        self.dense1 = nn.utils.weight_norm(nn.Linear(num_features, hidden_size))

        self.convBlock1 = ConvBlock(cha_1, cha_2, kernel_size=5, stride=1, padding=2, dropout_rate=0.1)

        self.ave_po_c1 = nn.AdaptiveAvgPool1d(output_size = cha_po_1)

        self.convBlock2 = ConvBlock(cha_2, cha_2, kernel_size=3, stride=1, padding=1, dropout_rate=0.1)
        self.convBlock3 = ConvBlock(cha_2, cha_2, kernel_size=3, stride=1, padding=1, dropout_rate=0.3)
        self.convBlock4 = ConvBlock(cha_2, cha_3, kernel_size=5, stride=1, padding=2, dropout_rate=0.2)

        self.max_po_c2 = nn.MaxPool1d(kernel_size=4, stride=2, padding=1)

        self.flt = nn.Flatten()

        self.batch_norm3 = nn.BatchNorm1d(cha_po_2)
        self.dropout3 = nn.Dropout(0.2)
        self.dense3 = nn.utils.weight_norm(nn.Linear(cha_po_2, num_targets))

        # Manual weights initialization
        for m in self.modules():
            if isinstance(m, nn.Conv1d):
                init.kaiming_normal_(m.weight)
            elif isinstance(m, nn.BatchNorm1d): # initialize for clarification
                init.constant_(m.weight, 1)
                init.constant_(m.bias, 0)

    def forward(self, x):
        x = self.batch_norm1(x)
        x = self.dropout1(x)
        x = F.celu(self.dense1(x), alpha=0.06)

        x = x.reshape(x.shape[0],self.cha_1, self.cha_1_reshape)

        x = self.convBlock1(x)

        x = self.ave_po_c1(x)

        x = self.convBlock2(x)
        x_s = x  # Saving for later use

        x = self.convBlock3(x)

        x = self.convBlock4(x)
        x = x * x_s  # Using saved value

        # Max pooling
        x = self.max_po_c2(x)

        # Flatten before final block
        x = self.flt(x)

        # Final block
        x = self.batch_norm3(x)
        x = self.dropout3(x)
        x = self.dense3(x)

        return x

# %% ../nbs/04_DL-multi.ipynb 45
def train_dl_multi(df, 
            feat_col1, 
            feat_col2,
            target_col,
            split, 
            model, 
             bs = 128,
            loss = mse, 
            save = None, # models/name.pth
             params = {'n_epoch': 4} # params in fastai Learner, e.g., lr_max
              ):
    
    train = df.loc[split[0]]
    valid = df.loc[split[1]]
    
    train_ds = DualInputDataset(train, feat_col1, feat_col2, target_col)
    valid_ds = DualInputDataset(valid, feat_col1, feat_col2, target_col)

    dls = DataLoaders.from_dsets(train_ds, valid_ds, bs=bs, num_workers=4)
    
    learn = Learner(dls.cuda(), model.cuda(), loss, metrics= [PearsonCorrCoef(),SpearmanCorrCoef()] )
    
    lr_max = learn.lr_find()
    plt.show()
    plt.close()
    print(lr_max)
    
    if 'lr_max' not in params:
        params['lr_max'] = lr_max
    
    print(f"lr_find is :{lr_max}, params lr is {params['lr_max']}")
    learn.fit_one_cycle(**params)
    
    if save is not None:
        learn.save(save)
    
    return learn

# %% ../nbs/04_DL-multi.ipynb 50
def predict_dl(df, 
               feat_col, 
               model, # model architecture
               model_pth, # only name, not with .pth
              ):
    test_dset = GeneralDataset(df,feat_col)
    test_dl = torch.utils.data.DataLoader(test_dset)
    
    
    learn = Learner(None, model.cuda(), loss_func=1)
    learn.load(model_pth)
    
    learn.model.eval()
    
    preds = []
    for data in test_dl:
        inputs = data.cuda()
        outputs = learn.model(inputs) #learn.model(x).sigmoid().detach().cpu().numpy()

        preds.append(outputs.detach().cpu().numpy())

    preds = np.concatenate(preds)
    preds = pd.DataFrame(preds)

    return preds
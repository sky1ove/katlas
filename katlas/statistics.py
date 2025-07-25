"""Functions for downstream analysis"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/08_statistics.ipynb.

# %% auto 0
__all__ = ['get_pvalue', 'get_metaP']

# %% ../nbs/08_statistics.ipynb 3
import pandas as pd

# P value session
import math
from scipy.stats import ttest_ind, mannwhitneyu, wilcoxon,chi2
from statsmodels.stats.multitest import multipletests

# %% ../nbs/08_statistics.ipynb 8
def get_pvalue(df,
              columns1, # list of column names for group1
              columns2, # list of column names for group2
              test_method = 'mann_whitney', # 'student_t', 'mann_whitney', 'wilcoxon'
              FC_method = 'median', # or mean
             ):

    "Performs statistical tests and calculates difference between the median or mean of two groups of columns."

    group1 = df[columns1]
    group2 = df[columns2]

    # Compute median values for each gene in both groups
    if FC_method == "median":
        m1 = group1.median(axis=1)
        m2 = group2.median(axis=1)
    elif FC_method == "mean":
        m1 = group1.mean(axis=1)
        m2 = group2.mean(axis=1)

    # As phosphoproteomics data has already been log transformed, we can directly use subtraction
    FCs = m2 - m1

    # Perform the chosen test and handle NaN p-values
    if test_method == 'student_t': # data is normally distributed, non-paired
        test_func = ttest_ind
    elif test_method == 'mann_whitney': # not normally distributed, non-paired, mann_whitney considers the rank, ignore the differences
        test_func = mannwhitneyu
    elif test_method == 'wilcoxon': # not normally distributed, paired
        test_func = wilcoxon

    t_results = []
    for idx in tqdm(df.index, desc=f"Computing {test_method} tests"):
        try:
            if test_method == 'wilcoxon': # as wilcoxon is paired, if lack a paired sample, just give nan, as default nanpolicy is propagate (gives nan if nan in input)
                stat, pvalue = test_func(group1.loc[idx], group2.loc[idx])
            else:
                stat, pvalue = test_func(group1.loc[idx], group2.loc[idx], nan_policy='omit')
        except ValueError:  # Handle cases with insufficient data
            pvalue = np.nan
        t_results.append(pvalue)

    # Exclude NaN p-values before multiple testing correction
    p_values = np.array(t_results, dtype=float)  # Ensure the correct data type
    valid_p_values = p_values[~np.isnan(p_values)]

    # Adjust for multiple testing on valid p-values only
    reject, pvals_corrected, _, _ = multipletests(valid_p_values, alpha=0.05, method='fdr_bh')

    # Create a full list of corrected p-values including NaNs
    full_pvals_corrected = np.full_like(p_values, np.nan)
    np.place(full_pvals_corrected, ~np.isnan(p_values), pvals_corrected)

    # Adjust the significance accordingly
    full_reject = np.zeros_like(p_values, dtype=bool)
    np.place(full_reject, ~np.isnan(p_values), reject)

    # Create DataFrame with results
    results = pd.DataFrame({
        'log2FC': FCs,
        'p_value': p_values,
        'p_adj': full_pvals_corrected
    })

    results['p_value'] = results['p_value'].astype(float)

    def get_signed_logP(r,p_col):
        log10 = -np.log10(r[p_col])
        return -log10 if r['log2FC']<0 else log10

    results['signed_logP'] = results.apply(partial(get_signed_logP,p_col='p_value'),axis=1)
    results['signed_logPadj'] = results.apply(partial(get_signed_logP,p_col='p_adj'),axis=1)

    return results

# %% ../nbs/08_statistics.ipynb 9
def get_metaP(p_values):
    
    "Use Fisher's method to calculate a combined p value given a list of p values; this function also allows negative p values (negative correlation)"

    logs = [math.log(abs(p))*-1 if p<0 else math.log(abs(p)) for p in p_values]
    chi_square_stat = -2 * sum(logs)
    degrees_of_freedom = 2 * len(p_values)
    score = chi2.sf(abs(chi_square_stat), degrees_of_freedom)*-1 if chi_square_stat<0 else chi2.sf(abs(chi_square_stat), degrees_of_freedom)

    return score

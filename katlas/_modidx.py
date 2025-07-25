# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/katlas',
                'doc_host': 'https://sky1ove.github.io',
                'git_url': 'https://github.com/sky1ove/katlas',
                'lib_path': 'katlas'},
  'syms': { 'katlas.align': { 'katlas.align.aln2df': ('alignment.html#aln2df', 'katlas/align.py'),
                              'katlas.align.get_aln_freq': ('alignment.html#get_aln_freq', 'katlas/align.py'),
                              'katlas.align.get_fasta': ('alignment.html#get_fasta', 'katlas/align.py'),
                              'katlas.align.run_clustalo': ('alignment.html#run_clustalo', 'katlas/align.py')},
            'katlas.analyze': { 'katlas.analyze.get_metaP': ('analyze.html#get_metap', 'katlas/analyze.py'),
                                'katlas.analyze.get_pvalue': ('analyze.html#get_pvalue', 'katlas/analyze.py')},
            'katlas.clustering': { 'katlas.clustering.get_1d_distance': ('hierarchical.html#get_1d_distance', 'katlas/clustering.py'),
                                   'katlas.clustering.get_1d_distance_parallel': ( 'hierarchical.html#get_1d_distance_parallel',
                                                                                   'katlas/clustering.py'),
                                   'katlas.clustering.get_1d_js': ('hierarchical.html#get_1d_js', 'katlas/clustering.py'),
                                   'katlas.clustering.get_1d_js_parallel': ('hierarchical.html#get_1d_js_parallel', 'katlas/clustering.py'),
                                   'katlas.clustering.get_Z': ('hierarchical.html#get_z', 'katlas/clustering.py'),
                                   'katlas.clustering.get_distance': ('hierarchical.html#get_distance', 'katlas/clustering.py'),
                                   'katlas.clustering.get_pssm_seq_labels': ( 'hierarchical.html#get_pssm_seq_labels',
                                                                              'katlas/clustering.py'),
                                   'katlas.clustering.js_divergence': ('hierarchical.html#js_divergence', 'katlas/clustering.py'),
                                   'katlas.clustering.js_divergence_flat': ('hierarchical.html#js_divergence_flat', 'katlas/clustering.py'),
                                   'katlas.clustering.plot_dendrogram': ('hierarchical.html#plot_dendrogram', 'katlas/clustering.py'),
                                   'katlas.clustering.pssm_to_seq': ('hierarchical.html#pssm_to_seq', 'katlas/clustering.py')},
            'katlas.core': {},
            'katlas.data': { 'katlas.data.CPTAC': ('data.html#cptac', 'katlas/data.py'),
                             'katlas.data.CPTAC._fetch_parquet': ('data.html#cptac._fetch_parquet', 'katlas/data.py'),
                             'katlas.data.CPTAC.get_id': ('data.html#cptac.get_id', 'katlas/data.py'),
                             'katlas.data.CPTAC.list_cancer': ('data.html#cptac.list_cancer', 'katlas/data.py'),
                             'katlas.data.Data': ('data.html#data', 'katlas/data.py'),
                             'katlas.data.Data._convert_numeric_columns': ('data.html#data._convert_numeric_columns', 'katlas/data.py'),
                             'katlas.data.Data.fetch_csv': ('data.html#data.fetch_csv', 'katlas/data.py'),
                             'katlas.data.Data.fetch_parquet': ('data.html#data.fetch_parquet', 'katlas/data.py'),
                             'katlas.data.Data.get_aa_info': ('data.html#data.get_aa_info', 'katlas/data.py'),
                             'katlas.data.Data.get_aa_morgan': ('data.html#data.get_aa_morgan', 'katlas/data.py'),
                             'katlas.data.Data.get_aa_rdkit': ('data.html#data.get_aa_rdkit', 'katlas/data.py'),
                             'katlas.data.Data.get_cddm': ('data.html#data.get_cddm', 'katlas/data.py'),
                             'katlas.data.Data.get_cddm_others': ('data.html#data.get_cddm_others', 'katlas/data.py'),
                             'katlas.data.Data.get_cddm_others_info': ('data.html#data.get_cddm_others_info', 'katlas/data.py'),
                             'katlas.data.Data.get_cddm_upper': ('data.html#data.get_cddm_upper', 'katlas/data.py'),
                             'katlas.data.Data.get_combine': ('data.html#data.get_combine', 'katlas/data.py'),
                             'katlas.data.Data.get_combine_site_phosphorylated': ( 'data.html#data.get_combine_site_phosphorylated',
                                                                                   'katlas/data.py'),
                             'katlas.data.Data.get_combine_site_psp_ochoa': ('data.html#data.get_combine_site_psp_ochoa', 'katlas/data.py'),
                             'katlas.data.Data.get_cptac_ensembl_site': ('data.html#data.get_cptac_ensembl_site', 'katlas/data.py'),
                             'katlas.data.Data.get_cptac_gene_site': ('data.html#data.get_cptac_gene_site', 'katlas/data.py'),
                             'katlas.data.Data.get_cptac_unique_site': ('data.html#data.get_cptac_unique_site', 'katlas/data.py'),
                             'katlas.data.Data.get_human_site': ('data.html#data.get_human_site', 'katlas/data.py'),
                             'katlas.data.Data.get_kd_uniprot': ('data.html#data.get_kd_uniprot', 'katlas/data.py'),
                             'katlas.data.Data.get_kinase_info': ('data.html#data.get_kinase_info', 'katlas/data.py'),
                             'katlas.data.Data.get_kinase_uniprot': ('data.html#data.get_kinase_uniprot', 'katlas/data.py'),
                             'katlas.data.Data.get_ks_background': ('data.html#data.get_ks_background', 'katlas/data.py'),
                             'katlas.data.Data.get_ks_dataset': ('data.html#data.get_ks_dataset', 'katlas/data.py'),
                             'katlas.data.Data.get_ks_unique': ('data.html#data.get_ks_unique', 'katlas/data.py'),
                             'katlas.data.Data.get_num_dict': ('data.html#data.get_num_dict', 'katlas/data.py'),
                             'katlas.data.Data.get_ochoa_site': ('data.html#data.get_ochoa_site', 'katlas/data.py'),
                             'katlas.data.Data.get_psp_human_site': ('data.html#data.get_psp_human_site', 'katlas/data.py'),
                             'katlas.data.Data.get_pspa_all_norm': ('data.html#data.get_pspa_all_norm', 'katlas/data.py'),
                             'katlas.data.Data.get_pspa_all_scale': ('data.html#data.get_pspa_all_scale', 'katlas/data.py'),
                             'katlas.data.Data.get_pspa_st_norm': ('data.html#data.get_pspa_st_norm', 'katlas/data.py'),
                             'katlas.data.Data.get_pspa_st_pct': ('data.html#data.get_pspa_st_pct', 'katlas/data.py'),
                             'katlas.data.Data.get_pspa_tyr_norm': ('data.html#data.get_pspa_tyr_norm', 'katlas/data.py'),
                             'katlas.data.Data.get_pspa_tyr_pct': ('data.html#data.get_pspa_tyr_pct', 'katlas/data.py'),
                             'katlas.data.Data.get_reactome_pathway': ('data.html#data.get_reactome_pathway', 'katlas/data.py'),
                             'katlas.data.Data.get_reactome_pathway_lo': ('data.html#data.get_reactome_pathway_lo', 'katlas/data.py')},
            'katlas.dl': { 'katlas.dl.CNN1D_1': ('dl.html#cnn1d_1', 'katlas/dl.py'),
                           'katlas.dl.CNN1D_1.__init__': ('dl.html#cnn1d_1.__init__', 'katlas/dl.py'),
                           'katlas.dl.CNN1D_1.forward': ('dl.html#cnn1d_1.forward', 'katlas/dl.py'),
                           'katlas.dl.CNN1D_2': ('dl.html#cnn1d_2', 'katlas/dl.py'),
                           'katlas.dl.CNN1D_2.__init__': ('dl.html#cnn1d_2.__init__', 'katlas/dl.py'),
                           'katlas.dl.CNN1D_2.forward': ('dl.html#cnn1d_2.forward', 'katlas/dl.py'),
                           'katlas.dl.GeneralDataset': ('dl.html#generaldataset', 'katlas/dl.py'),
                           'katlas.dl.GeneralDataset.__getitem__': ('dl.html#generaldataset.__getitem__', 'katlas/dl.py'),
                           'katlas.dl.GeneralDataset.__init__': ('dl.html#generaldataset.__init__', 'katlas/dl.py'),
                           'katlas.dl.GeneralDataset.__len__': ('dl.html#generaldataset.__len__', 'katlas/dl.py'),
                           'katlas.dl.MLP_1': ('dl.html#mlp_1', 'katlas/dl.py'),
                           'katlas.dl.conv_wn': ('dl.html#conv_wn', 'katlas/dl.py'),
                           'katlas.dl.get_sampler': ('dl.html#get_sampler', 'katlas/dl.py'),
                           'katlas.dl.init_weights': ('dl.html#init_weights', 'katlas/dl.py'),
                           'katlas.dl.lin_wn': ('dl.html#lin_wn', 'katlas/dl.py'),
                           'katlas.dl.predict_dl': ('dl.html#predict_dl', 'katlas/dl.py'),
                           'katlas.dl.seed_everything': ('dl.html#seed_everything', 'katlas/dl.py'),
                           'katlas.dl.train_dl': ('dl.html#train_dl', 'katlas/dl.py'),
                           'katlas.dl.train_dl_cv': ('dl.html#train_dl_cv', 'katlas/dl.py')},
            'katlas.feature': { 'katlas.feature.get_clusters_elbow': ('feature.html#get_clusters_elbow', 'katlas/feature.py'),
                                'katlas.feature.get_esm': ('feature.html#get_esm', 'katlas/feature.py'),
                                'katlas.feature.get_morgan': ('feature.html#get_morgan', 'katlas/feature.py'),
                                'katlas.feature.get_rdkit': ('feature.html#get_rdkit', 'katlas/feature.py'),
                                'katlas.feature.get_rdkit_3d': ('feature.html#get_rdkit_3d', 'katlas/feature.py'),
                                'katlas.feature.get_rdkit_all': ('feature.html#get_rdkit_all', 'katlas/feature.py'),
                                'katlas.feature.get_rdkit_df': ('feature.html#get_rdkit_df', 'katlas/feature.py'),
                                'katlas.feature.get_t5': ('feature.html#get_t5', 'katlas/feature.py'),
                                'katlas.feature.get_t5_bfd': ('feature.html#get_t5_bfd', 'katlas/feature.py'),
                                'katlas.feature.onehot_encode': ('feature.html#onehot_encode', 'katlas/feature.py'),
                                'katlas.feature.preprocess': ('feature.html#preprocess', 'katlas/feature.py'),
                                'katlas.feature.remove_hi_corr': ('feature.html#remove_hi_corr', 'katlas/feature.py'),
                                'katlas.feature.standardize': ('feature.html#standardize', 'katlas/feature.py')},
            'katlas.pathway': { 'katlas.pathway.add_react_ref': ('pathway.html#add_react_ref', 'katlas/pathway.py'),
                                'katlas.pathway.get_reactome': ('pathway.html#get_reactome', 'katlas/pathway.py'),
                                'katlas.pathway.get_reactome_raw': ('pathway.html#get_reactome_raw', 'katlas/pathway.py'),
                                'katlas.pathway.plot_overlap': ('pathway.html#plot_overlap', 'katlas/pathway.py'),
                                'katlas.pathway.plot_path': ('pathway.html#plot_path', 'katlas/pathway.py'),
                                'katlas.pathway.query_reactome': ('pathway.html#query_reactome', 'katlas/pathway.py')},
            'katlas.plot': { 'katlas.plot.get_AUCDF': ('plot.html#get_aucdf', 'katlas/plot.py'),
                             'katlas.plot.get_color_dict': ('plot.html#get_color_dict', 'katlas/plot.py'),
                             'katlas.plot.get_hue_big': ('plot.html#get_hue_big', 'katlas/plot.py'),
                             'katlas.plot.get_pct': ('plot.html#get_pct', 'katlas/plot.py'),
                             'katlas.plot.get_plt_color': ('plot.html#get_plt_color', 'katlas/plot.py'),
                             'katlas.plot.get_similarity': ('plot.html#get_similarity', 'katlas/plot.py'),
                             'katlas.plot.plot_2d': ('plot.html#plot_2d', 'katlas/plot.py'),
                             'katlas.plot.plot_bar': ('plot.html#plot_bar', 'katlas/plot.py'),
                             'katlas.plot.plot_bokeh': ('plot.html#plot_bokeh', 'katlas/plot.py'),
                             'katlas.plot.plot_box': ('plot.html#plot_box', 'katlas/plot.py'),
                             'katlas.plot.plot_cluster': ('plot.html#plot_cluster', 'katlas/plot.py'),
                             'katlas.plot.plot_cnt': ('plot.html#plot_cnt', 'katlas/plot.py'),
                             'katlas.plot.plot_composition': ('plot.html#plot_composition', 'katlas/plot.py'),
                             'katlas.plot.plot_confusion_matrix': ('plot.html#plot_confusion_matrix', 'katlas/plot.py'),
                             'katlas.plot.plot_corr': ('plot.html#plot_corr', 'katlas/plot.py'),
                             'katlas.plot.plot_count': ('plot.html#plot_count', 'katlas/plot.py'),
                             'katlas.plot.plot_group_bar': ('plot.html#plot_group_bar', 'katlas/plot.py'),
                             'katlas.plot.plot_hist': ('plot.html#plot_hist', 'katlas/plot.py'),
                             'katlas.plot.plot_matrix': ('plot.html#plot_matrix', 'katlas/plot.py'),
                             'katlas.plot.plot_pie': ('plot.html#plot_pie', 'katlas/plot.py'),
                             'katlas.plot.plot_rank': ('plot.html#plot_rank', 'katlas/plot.py'),
                             'katlas.plot.plot_stacked': ('plot.html#plot_stacked', 'katlas/plot.py'),
                             'katlas.plot.reduce_feature': ('plot.html#reduce_feature', 'katlas/plot.py'),
                             'katlas.plot.save_pdf': ('plot.html#save_pdf', 'katlas/plot.py'),
                             'katlas.plot.save_show': ('plot.html#save_show', 'katlas/plot.py'),
                             'katlas.plot.save_svg': ('plot.html#save_svg', 'katlas/plot.py'),
                             'katlas.plot.set_sns': ('plot.html#set_sns', 'katlas/plot.py')},
            'katlas.pssm': { 'katlas.pssm.change_center_name': ('pssm.html#change_center_name', 'katlas/pssm.py'),
                             'katlas.pssm.clean_zero_normalize': ('pssm.html#clean_zero_normalize', 'katlas/pssm.py'),
                             'katlas.pssm.convert_logo_df': ('pssm.html#convert_logo_df', 'katlas/pssm.py'),
                             'katlas.pssm.entropy': ('pssm.html#entropy', 'katlas/pssm.py'),
                             'katlas.pssm.entropy_flat': ('pssm.html#entropy_flat', 'katlas/pssm.py'),
                             'katlas.pssm.flatten_pssm': ('pssm.html#flatten_pssm', 'katlas/pssm.py'),
                             'katlas.pssm.get_IC_per_position': ('pssm.html#get_ic_per_position', 'katlas/pssm.py'),
                             'katlas.pssm.get_IC_per_position_flat': ('pssm.html#get_ic_per_position_flat', 'katlas/pssm.py'),
                             'katlas.pssm.get_cluster_pssms': ('pssm.html#get_cluster_pssms', 'katlas/pssm.py'),
                             'katlas.pssm.get_logo': ('pssm.html#get_logo', 'katlas/pssm.py'),
                             'katlas.pssm.get_one_kinase': ('pssm.html#get_one_kinase', 'katlas/pssm.py'),
                             'katlas.pssm.get_pos_min_max': ('pssm.html#get_pos_min_max', 'katlas/pssm.py'),
                             'katlas.pssm.get_prob': ('pssm.html#get_prob', 'katlas/pssm.py'),
                             'katlas.pssm.get_pssm_IC': ('pssm.html#get_pssm_ic', 'katlas/pssm.py'),
                             'katlas.pssm.get_pssm_IC_standard': ('pssm.html#get_pssm_ic_standard', 'katlas/pssm.py'),
                             'katlas.pssm.get_pssm_LO': ('pssm.html#get_pssm_lo', 'katlas/pssm.py'),
                             'katlas.pssm.pSTY2sty': ('pssm.html#psty2sty', 'katlas/pssm.py'),
                             'katlas.pssm.plot_heatmap': ('pssm.html#plot_heatmap', 'katlas/pssm.py'),
                             'katlas.pssm.plot_heatmap_simple': ('pssm.html#plot_heatmap_simple', 'katlas/pssm.py'),
                             'katlas.pssm.plot_logo': ('pssm.html#plot_logo', 'katlas/pssm.py'),
                             'katlas.pssm.plot_logo_LO': ('pssm.html#plot_logo_lo', 'katlas/pssm.py'),
                             'katlas.pssm.plot_logo_heatmap': ('pssm.html#plot_logo_heatmap', 'katlas/pssm.py'),
                             'katlas.pssm.plot_logo_heatmap_LO': ('pssm.html#plot_logo_heatmap_lo', 'katlas/pssm.py'),
                             'katlas.pssm.plot_logo_raw': ('pssm.html#plot_logo_raw', 'katlas/pssm.py'),
                             'katlas.pssm.plot_logos': ('pssm.html#plot_logos', 'katlas/pssm.py'),
                             'katlas.pssm.plot_logos_idx': ('pssm.html#plot_logos_idx', 'katlas/pssm.py'),
                             'katlas.pssm.raw2norm': ('pssm.html#raw2norm', 'katlas/pssm.py'),
                             'katlas.pssm.recover_pssm': ('pssm.html#recover_pssm', 'katlas/pssm.py'),
                             'katlas.pssm.scale_pos_neg_values': ('pssm.html#scale_pos_neg_values', 'katlas/pssm.py'),
                             'katlas.pssm.scale_zero_position': ('pssm.html#scale_zero_position', 'katlas/pssm.py')},
            'katlas.score': { 'katlas.score.Params': ('score.html#params', 'katlas/score.py'),
                              'katlas.score.STY2sty': ('score.html#sty2sty', 'katlas/score.py'),
                              'katlas.score.calculate_log_odds': ('score.html#calculate_log_odds', 'katlas/score.py'),
                              'katlas.score.check_seqs': ('score.html#check_seqs', 'katlas/score.py'),
                              'katlas.score.cut_seq': ('score.html#cut_seq', 'katlas/score.py'),
                              'katlas.score.cut_seq_on_pssms': ('score.html#cut_seq_on_pssms', 'katlas/score.py'),
                              'katlas.score.cut_seq_on_pssms_df': ('score.html#cut_seq_on_pssms_df', 'katlas/score.py'),
                              'katlas.score.get_dict': ('score.html#get_dict', 'katlas/score.py'),
                              'katlas.score.get_kinase_log_odds': ('score.html#get_kinase_log_odds', 'katlas/score.py'),
                              'katlas.score.get_kinase_log_odds_df': ('score.html#get_kinase_log_odds_df', 'katlas/score.py'),
                              'katlas.score.get_pct': ('score.html#get_pct', 'katlas/score.py'),
                              'katlas.score.get_pct_df': ('score.html#get_pct_df', 'katlas/score.py'),
                              'katlas.score.get_pos_range': ('score.html#get_pos_range', 'katlas/score.py'),
                              'katlas.score.multiply': ('score.html#multiply', 'katlas/score.py'),
                              'katlas.score.multiply_func': ('score.html#multiply_func', 'katlas/score.py'),
                              'katlas.score.predict_kinase': ('score.html#predict_kinase', 'katlas/score.py'),
                              'katlas.score.predict_kinase_df': ('score.html#predict_kinase_df', 'katlas/score.py'),
                              'katlas.score.sumup': ('score.html#sumup', 'katlas/score.py')},
            'katlas.statistics': { 'katlas.statistics.get_metaP': ('statistics.html#get_metap', 'katlas/statistics.py'),
                                   'katlas.statistics.get_pvalue': ('statistics.html#get_pvalue', 'katlas/statistics.py')},
            'katlas.train': { 'katlas.train.get_splits': ('ml.html#get_splits', 'katlas/train.py'),
                              'katlas.train.predict_ml': ('ml.html#predict_ml', 'katlas/train.py'),
                              'katlas.train.score_each': ('ml.html#score_each', 'katlas/train.py'),
                              'katlas.train.split_data': ('ml.html#split_data', 'katlas/train.py'),
                              'katlas.train.train_ml': ('ml.html#train_ml', 'katlas/train.py'),
                              'katlas.train.train_ml_cv': ('ml.html#train_ml_cv', 'katlas/train.py')},
            'katlas.utils': { 'katlas.utils.check_seq': ('utils.html#check_seq', 'katlas/utils.py'),
                              'katlas.utils.check_seq_df': ('utils.html#check_seq_df', 'katlas/utils.py'),
                              'katlas.utils.check_seqs': ('utils.html#check_seqs', 'katlas/utils.py'),
                              'katlas.utils.extract_site_seq': ('utils.html#extract_site_seq', 'katlas/utils.py'),
                              'katlas.utils.get_diff': ('utils.html#get_diff', 'katlas/utils.py'),
                              'katlas.utils.get_path': ('utils.html#get_path', 'katlas/utils.py'),
                              'katlas.utils.phosphorylate_seq': ('utils.html#phosphorylate_seq', 'katlas/utils.py'),
                              'katlas.utils.phosphorylate_seq_df': ('utils.html#phosphorylate_seq_df', 'katlas/utils.py'),
                              'katlas.utils.validate_site': ('utils.html#validate_site', 'katlas/utils.py'),
                              'katlas.utils.validate_site_df': ('utils.html#validate_site_df', 'katlas/utils.py')}}}

def dictionary_learning_MHOF(flow_hist_H_400):
    from sklearn.decomposition import MiniBatchDictionaryLearning
    dico=MiniBatchDictionaryLearning(n_components=400,alpha=1,n_iter=500)
    dic=dico.fit(flow_hist_H_400).components_
    #coeffs=dico.transform(flow_hist_H_400)
    return dic
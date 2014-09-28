def coeff_MHOF(dic,flow_hist_H):
    import numpy as np
    import scipy.io
    flow_hist_H=np.reshape(flow_hist_H,[1,flow_hist_H.size])
    #D_I=scipy.io.loadmat('dic_400_inv.mat')
    #D_I=D_I['D_I']
    #D_I=np.lialg.pinv(dic)
    D_I=scipy.io.loadmat('dic_400_I.mat')
    D_I=D_I['dic_I']
    coeff=np.dot(D_I.T,flow_hist_H.T)
    #from sklearn.decomposition import SparseCoder
    #flow_hist_H=np.reshape(flow_hist_H,[1,flow_hist_H.size])
    #coder=SparseCoder(dictionary=dic)
    #coeff=coder.transform(flow_hist_H)
    return coeff
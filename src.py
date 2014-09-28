def src(dic,coeff,flow_hist_H,lamda=0.1):
    import numpy as np
    flow_hist_H=np.reshape(flow_hist_H,[1,flow_hist_H.size])
    #coeff=np.reshape(coeff,[1,coeff.size])
    diff=flow_hist_H-np.dot(coeff.T,dic)
    src=0.5*np.linalg.norm(diff,2)+lamda*np.linalg.norm(coeff,1)
    return src
def dictionay_learning_MHOF_online(training_samples_num=400):
    from MHOF_Extraction import MHOF_Extraction
    from MHOF_histogram_block import MHOF_histogram_block
    from sklearn.decomposition import MiniBatchDictionaryLearning
    import numpy as np
    import cv2
    import video
    cam=video.create_capture('Crowd-Activity-All.avi')
    height_block_num=4
    width_block_num=5
    bin_num=16
    ret,prev=cam.read()
    ret,img=cam.read()
    flow_H=MHOF_Extraction(prev,img)
    flow_hist_H=MHOF_histogram_block(flow_H,height_block_num,width_block_num,bin_num)
    flow_hist_H=np.reshape(flow_hist_H,[1,flow_hist_H.size])
    #  error!!!!
    dico=MiniBatchDictionaryLearning(1,alpha=1,n_iter=500)
    dic=dico.fit(flow_hist_H).components_
    for i in range(training_samples_num):
        ret,img=cam.read()
        flow_H=MHOF_Extraction(prev,img)
        flow_hist_H=MHOF_histogram_block(flow_H,height_block_num,width_block_num,bin_num)
        dico=MiniBatchDictionaryLearing(i+1,alpha=1,n_iter=500,dict_init=dic)
        dic=dico.fit(flow_hist_H).components
    return dic

        
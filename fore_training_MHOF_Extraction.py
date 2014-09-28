def fore_training_MHOF_Extraction(training_samples_num=400):
    from MHOF_Extraction import MHOF_Extraction
    import numpy as np
    import cv2
    import video
    cam=video.create_capture('Crowd-Activity-All.avi')
    height_block_num=4
    width_block_num=5
    bin_num=16
    flow_hist_H_400=np.zeros([training_samples_num,height_block_num*width_block_num*bin_num])
    ret,prev=cam.read()
    for i in range(training_samples_num):
        ret,img=cam.read()
        flow_H=MHOF_Extraction(prev,img)
        from MHOF_histogram_block import MHOF_histogram_block
        flow_hist_H=MHOF_histogram_block(flow_H,height_block_num,width_block_num,bin_num)
        flow_hist_H_400[i,:]=flow_hist_H
        prev=img
    return flow_hist_H_400


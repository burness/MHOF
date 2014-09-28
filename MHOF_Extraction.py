#/usr/bin/env python

import numpy as np
import cv2
import video
def MHOF_Extraction(prev,img):
    import sys
    prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, 0.5, 3, 15, 3, 5, 1.2, 0)
    vx=flow[:,:,0]
    vy=flow[:,:,1]
    m,n=vx.shape
    prevgray = gray
    Bin_num=16
    tao=1
    flow_motion=vx**2+vy**2
    flow_direction=np.arctan2(vx,vy)
    flow_direction=np.array(flow_direction<0,dtype=int)*2*np.pi+flow_direction
    flow_H=np.array(flow_motion>1)*(Bin_num/2)+np.mod(np.round(flow_direction*Bin_num*0.5/(2*np.pi)),0.5*Bin_num)

    return flow_H




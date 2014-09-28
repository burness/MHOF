from __future__ import division
from MHOF_Extraction import MHOF_Extraction
import numpy as np
import scipy.io
import cv2
import video
from coeff_MHOF import coeff_MHOF
from MHOF_histogram_block import MHOF_histogram_block
from src import src
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
cam=video.create_capture('Crowd-Activity-All.avi')
cv2.namedWindow('frame',1)
dic=np.load('dic_400.npy')
#dic=scipy.io.loadmat('dic_400.mat')
#dic=dic['Dksvd']
ret,prev=cam.read()
n=0
while 1:
    ret,img=cam.read()
    s=time.clock()
    flow_H=MHOF_Extraction(prev,img)
    flow_hist_H=MHOF_histogram_block(flow_H,4,5,16)
    coeff=coeff_MHOF(dic,flow_hist_H) 
    src_MHOF=src(dic,coeff,flow_hist_H)
    cv2.imshow('frame',img)
    c=cv2.waitKey(1)
    n+=1
    prev=img
    if c==27:
        break
    str='frame:(%s) src:(%s),time:(%s)'%(n,src_MHOF/1000,time.clock()-s)
    print str
from fore_training_MHOF_Extraction import fore_training_MHOF_Extraction
import numpy as np
flow_hist_H_400=fore_training_MHOF_Extraction(400)
np.save('flow_hist_H_400',flow_hist_H_400)
#flow_hist_H_400=np.load('flow_hist_H_400.npy')
from dictionary_learning_MHOF import dictionary_learning_MHOF
dic=dictionary_learning_MHOF(flow_hist_H_400)
np.save('dic_400',dic)
# no overlap implemention
def MHOF_histogram_block(flow_H,height_block_num,width_block_num,bin_num):
    import numpy as np
    m,n=flow_H.shape
    height_per_block=m/height_block_num
    width_per_block=n/width_block_num
    flow_hist_H=np.zeros([height_block_num*width_block_num,bin_num])
    for i in range(height_block_num):
        for j in range(width_block_num):
            # get subblock
            flow_per_block=flow_H[i*height_per_block:(i+1)*height_per_block-1,j*height_per_block:(j+1)*height_per_block-1]
            # compute the histogram between 0 and 15 of every block
            for k in range(bin_num):
                flow_hist_H[i*width_block_num+j,k]=np.sum(np.array(flow_per_block==k,dtype=int))
    flow_hist_H=np.reshape(flow_hist_H,[height_block_num*width_block_num*16])
    return flow_hist_H
                
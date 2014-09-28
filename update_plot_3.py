import time
import numpy as np
import matplotlib
matplotlib.use('WXAgg')
import matplotlib.pyplot as plt
import shutil
import wx

def pretreat(file_path):
    f=open(file_path, 'r')
    data1=f.readlines()
    f.close()
    data1[0:3]=[]
    data1[-1:]=[]
    data2=[i.strip() for i in data1]
    data3=[i.rstrip('?') for i in data2]
    data4=[i.strip() for i in data3]
    data5=[i.rstrip('g') for i in data4]
    data6=[i.strip() for i in data5]
    data7=[float(i) for i in data6]
    return data7

def update_line(idleevent):
    shutil.copyfile('data.log', 'temp.txt')
    path="temp.txt"
    data=pretreat(path)
    x=range(0,len(data))
    line.set_ydata(data)
    line.set_xdata(x)
    ax.set_xlim(0, len(data)+200)
    ax.set_ylim(data[len(data)-1]-50,data[0]+50)
    fig.canvas.draw_idle()
    time.sleep(2)

fig = plt.figure()
ax = fig.add_subplot(111)
shutil.copyfile('data.log', 'temp.txt')
path="temp.txt"
data=pretreat(path)
x=range(0,len(data))
ax.set_xlim(0, len(data)+200)
ax.set_ylim(data[len(data)-1]-50,data[0]+50)
line, = ax.plot(x,data)

wx.EVT_IDLE(wx.GetApp(), update_line)
plt.xlabel('Time (x10s)')
plt.ylabel('Weight (g)')
plt.title('Plotting')
plt.show()
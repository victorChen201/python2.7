#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi
from matplotlib.pyplot import step, legend, xlim, ylim, show
from matplotlib import rc, font_manager
from matplotlib.dates import datestr2num,DateFormatter
import math
import datetime
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
plt.style.use('ggplot')
data = pd.read_csv("airpollutants.csv",parse_dates=True, index_col='datetime')
# data1=data.resample('D').mean()
# data1=data1['2016-9-01':'2016-9-30']
# prepare for the loop 
list1=[]
list1=data.columns.values.tolist()
bar1list=list1[0:7] #OC ,EC, sulfate, nitrate, ammonia ,chlorine ,potassoium, cac
#文件名
filename="Time series of "+str(len(bar1list))+" species.pdf"
#数据
#data1,bar1list为需要分析的物种
f, ax1 = plt.subplots(1, figsize=(10,5))#
#设置bar 大小
bar_width = 0.8
#设置透明度大小
alphavalue=0.8
#设置字体及大小
SMALL_SIZE = 8
MEDIUM_SIZE = 9
BIGGER_SIZE = 12
ticks_font = font_manager.FontProperties(family='Arial', style='normal',
    size=6, weight='normal', stretch='normal')
#设置颜色
color1=['b','k','r','g','m','y','c','k','darkgreen']

# positions of the x-axis ticks (center of the bars as bar labels)
bar_l = [i+1 for i in range(len(data[bar1list[0]]))]
tick_pos = [i+(bar_width/2) for i in bar_l] 

margin_bottom = np.zeros(len(data[bar1list[0]]))
for i in range(len(bar1list)):
    pdname=bar1list[i]
    ax1.bar(bar_l,data[pdname], width=bar_width,label=pdname,alpha=alphavalue,color=color1[i],bottom=margin_bottom, linewidth=0)
    margin_bottom += data[pdname]
#set axis font
axis_font = {'fontname':'Arial', 'size':'9'}
# ax1.set_xlabel('Time series', **axis_font)
ax1.set_ylabel(r'Mass concentration ($\mu$g/$m^3$)', **axis_font)
#set legend distribution and border
nlines = len(bar1list)
ncol = int(math.ceil(nlines/2.))
legend = plt.legend(ncol=ncol, loc='upper left')
legend.get_frame().set_facecolor('none')
legend.get_frame().set_linewidth(0.0)
#隐藏xticks
ax1.xaxis.set_ticks_position('none') 
#设置xtickslabel 位置及格式
justdate=data.index.strftime('%Y-%m-%d')
plt.xticks(tick_pos, justdate)
ax1.set_xticklabels(justdate, rotation=90)
#设置x y 长度及刻度                  
plt.xlim([min(tick_pos)-bar_width/1.5, max(tick_pos)+bar_width/1.5])
#设置字体之类
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
#保存图片
plt.savefig(filename, bbox_inches='tight')
plt.show()

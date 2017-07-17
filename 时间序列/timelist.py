#!/usr/bin/env python
# -*- conding: utf-8 -*-
import pandas as pd
import numpy as np
import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import matplotlib.ticker as mpt
import matplotlib as mpl

from matplotlib.dates import DateFormatter, MonthLocator, DayLocator
ymajorLocator = mpt.MultipleLocator(20)
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 10,
        }
color_index = ['b', 'k', 'r', 'g', 'm', 'yellow','c']

df = pd.read_csv("sample.csv", parse_dates=True, index_col= 'datetime')

#ax3= plt.subplot(3, 1, 1)
fig, (ax1,ax2,ax3) = plt.subplots(3, 1, figsize = (10, 16))
#print df.values.shape
index = np.arange(df.values.shape[0])
#print 'index=',index
num = -1
bottomvalues = [0*len(df.index)]#df['OC'].values - df['OC'].values

#ax2.set_ylim(0,200)
legendArrar=[]
for i in df.columns:
    if i != 'datetime' and i != 'OC/EC' and i != 'S/N' and i != 'K/EC' and i != 'Ca' and i != 'Na' and i != 'Mg':
        num = num + 1
        ax3.bar(df.index, df[i].values, width = .8, color = color_index[num%7], bottom = bottomvalues, alpha = .7)
        bottomvalues = df[i].values + bottomvalues
        ax3.yaxis.label.set_color(num%7)
        legendArrar.append(i)

#ax3.legend(legendArrar, loc='upper right',ncol= 1)
ax3.legend(legendArrar, loc= 'upper center', bbox_to_anchor=(0.6,1.0),ncol=4,fancybox=True,shadow=False, fontsize = 8)
#set label
ax3.set_ylabel('Mass concentration (ug/m3)', fontdict=font)
#she zhi wang ge gao du
ax3.yaxis.set_major_locator(ymajorLocator)
#she zhi zuo biao ke du
#ax3.set_xticks([x for x in range(max(index) + 1)] )
#ax3.set_xticklabels(df['datetime'].values,rotation= 90)

#[datetime.strptime(d,'%m/%d/%Y').date() for d in df['datetime'].values]
ax3.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

ax3.xaxis.set_major_locator(DayLocator())
#ax3.xaxis.set_minor_locator(DayLocator())
#plt.tick_params(labelsize=8)
plt.setp(plt.gca().get_xticklabels(), rotation = 90, horizontalalignment = 'left')
#plt.setp(ax3,spines.values(), linewidth=0.4)
#print plt.gca().get_xticklabels()
Collist=['SN', 'OC/EC',['OC', 'EC', 'sulfate', 'nitrate', 'ammonia', 'chlorine', 'potassoiun']]
Plottypelist= ['line', 'stack', 'bar']
directions=['L', 'L', 'L']
colors=['r', 'g',['r', 'g','b',  'gold', 'navy', 'deeppink', 'tomato']]
plt.grid()
plt.show()

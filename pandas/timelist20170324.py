#!/usr/bin/env python
#-*-coding:utf-8-*-
import pandas as pd
import numpy as np
import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import matplotlib.ticker as mpt
import matplotlib as mpl
import types
from matplotlib.dates import DateFormatter, MonthLocator, DayLocator
#import sys
#reload(sys)
#sys.setdefaultencoding('gb18030')
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 10,
        }

color_index = ['b', 'r', 'c', 'g', 'm', 'yellow','c']
sprdeadline=['2013-03-01','2013-05-31']
sumdeadline=['2013-06-01','2013-08-31']
autdeadline=['2013-09-01','2013-11-30']
windeadline=['2013-12-01','2013-12-31']
season={'sp':sprdeadline,
        'sum':sumdeadline,
        'aut':autdeadline,
        'win':windeadline,
        }

collist=['NO', 'NO2', 'NOx', 'SO2', 'O3']
legend=['Spring', 'Summer', 'Autumn', 'Winter']
df = pd.read_csv("t2013.csv", parse_dates=True, index_col= 'TimePoint')
meanValues=[]
meanValues.append(df.loc[sprdeadline[0]:sprdeadline[1],collist].mean())
meanValues.append(df.loc[sumdeadline[0]:sumdeadline[1],collist].mean())
meanValues.append(df.loc[autdeadline[0]:autdeadline[1],collist].mean())
meanValues.append(df.loc[windeadline[0]:windeadline[1],collist].mean())
plt.style.use('classic')
ax3= plt.subplot(1, 1, 1)
#fig, (ax1,ax2,ax3) = plt.subplots(3, 1, figsize = (10, 16))
#print df.values.shape
index = np.arange(len(collist))
#print 'index=',index
#num = -1
#bottomvalues = [0*len(df.index)]#df['OC'].values - df['OC'].values

#ax2.set_ylim(0,200)
#legendArrar=[]
temp=index
for i in range(len(season)):
#    if i != 'datetime' and i != 'OC/EC' and i != 'S/N' and i != 'K/EC' and i != 'Ca' and i != 'Na' and i != 'Mg':
#        num = num + 1
    print meanValues[i].values
#        ax3.bar(index+.5, spring.values, width = .8, color = color_index[i%7], alpha = .7)
    ax3.bar(temp , meanValues[i].values, width = .2, color = color_index[i%7], alpha = .7)
    temp=temp+0.2
#        bottomvalues = df[i].values + bottomvalues
#        ax3.yaxis.label.set_color(num%7)
#        legendArrar.append(i)

#ax3.legend(legendArrar, loc='upper right',ncol= 1)
ax3.legend(legend, loc= 'upper right', ncol=2, fancybox=True, shadow=False, fontsize = 8)
#set label
#ax3.set_ylabel('Mass concentration (ug/m3)', fontdict=font)
#she zhi wang ge gao du
#ax3.yaxis.set_major_locator(ymajorLocator)
#she zhi zuo biao ke du
ax3.set_xticks([x+0.2*2 for x in range(max(index) + 1)] )
ax3.set_xticklabels(collist)
ax3.set_ylabel(u'质量浓度(ug/m3)',fontdict= font)
#ax3.set_ylabel('质量浓度(ug/m3)'.decode('utf'),fontdict= font)
#[datetime.strptime(d,'%m/%d/%Y').date() for d in df['datetime'].values]
#ax3.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

#ax3.xaxis.set_major_locator(DayLocator())
#ax3.xaxis.set_minor_locator(DayLocator())
#plt.tick_params(labelsize=8)
#plt.setp(plt.gca().get_xticklabels(), rotation = 90, horizontalalignment = 'left')
#plt.setp(ax3,spines.values(), linewidth=0.4)
#print plt.gca().get_xticklabels()
#Collist=['SN', 'OC/EC',['OC', 'EC', 'sulfate', 'nitrate', 'ammonia', 'chlorine', 'potassoiun']]
#Plottypelist= ['line', 'stack', 'bar']
#directions=['L', 'L', 'L']
#colors=['r', 'g',['r', 'g','b',  'gold', 'navy', 'deeppink', 'tomato']]
#plt.grid()
plt.show()

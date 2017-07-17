#! /usr/bin/env python
# -*- conding: utf-8 -*-
#import matplotlib
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.dates import DateFormatter, DayLocator
font = {'family': 'serif',
        'color' : 'darkred',
        'weight': 'normal',
        'size'  : 10,
        }
axis_font = {'fontname':'Arial', 'size':'8'}

def multiplot(df, collist, plottypelist, directions, colorlist):
    axnum=len(collist)
#    plt.style.use('classic')
    bottomsum=[0*len(df.index)]
    print axnum
    for i in range(axnum):
        ax = plt.subplot(axnum,1,i+1)
        if 'line' == plottypelist[i]:
            ax.plot(df.index, df[collist[i]], linewidth= 0.4, color= colorlist[i])
            ax.get_xaxis().set_ticks([])
            plt.title(collist[i])
        elif 'bar' == plottypelist[i]:
            plt.bar(df.index,df[collist[i]], alpha = .5,color = colorlist[i])
            ax.get_xaxis().set_ticks([])
            plt.title(collist[i])
        elif 'stack' == plottypelist[i]:
            for j in range(len(collist[i])):
                ax.bar(df.index, df[collist[i][j]], width= .8, color= colorlist[i][j], bottom=bottomsum, alpha = .7)
                bottomsum = bottomsum + df[collist[i][j]]
            plt.legend(collist[i], ncol = len(collist[i])/2, loc = 'upper center', bbox_to_anchor=(0.6, 1.0), fancybox=True, shadow=False, fontsize= 8)
            ax.set_ylabel('Mass concentration (ug/m3)', fontdict = font)
            ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
            ax.xaxis.set_major_locator(DayLocator())
            plt.setp(plt.gca().get_xticklabels(), rotation = 90, horizontalalignment = 'left')
            plt.grid()
        else:
            print 'Type error!!\n'
    plt.show()
    return 0
df = pd.read_csv('sample.csv', parse_dates = True, index_col = 'datetime')
collist= ['S/N', 'OC/EC', ['EC', 'sulfate', 'nitrate', 'ammonia', 'chlorine', 'potassoium']]
plottypelist= ['line', 'bar', 'stack']
directions= ['L', 'L', 'L']
colors= ['r','g',['r', 'g', 'b', 'gold', 'navy',  'tomato']]
multiplot(df,collist,plottypelist,directions,colors)

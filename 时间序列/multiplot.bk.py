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
    bottomsum=[0*len(df.index)]
    plt.style.use('classic')
    for i in range(axnum):
        ax = plt.subplot(axnum,1,i+1)
        if 'line' == plottypelist[i]:
            if isinstance(collist[i],str): #list, str,int,etc
                ax.plot(df.index, df[collist[i]], linewidth= 0.4, color= colorlist[i])
                ax.get_xaxis().set_ticks([])
                plt.title(collist[i])
            elif isinstance(collist[i],list):
                x=[collist[i][l] for l in range(len(directions[i])) if directions[i][l] == 'R']
                df1=df[collist[i]]
                if 'R' in directions[i]:
                    df1.plot(kind='line', ax=i, sharex=True, secondary_y=x)

                else:
                    df1.plot(kind='line')
            else:
                print 'Collist type error'
        elif 'bar' == plottypelist[i]:
            plt.bar(df.index,df[collist[i]], alpha = .5,color = colorlist[i])
            ax.get_xaxis().set_ticks([])
            plt.title(collist[i])
        elif 'stack' == plottypelist[i]:
            for j in range(len(collist[i])):
                ax.bar(df.index, df[collist[i][j]], width= .8, color= colorlist[i][j], bottom=bottomsum, alpha = .7)
                bottomsum = bottomsum + df[collist[i][j]]
            plt.legend(collist[i], ncol = len(collist[i])/2+1, loc = 'upper center', bbox_to_anchor=(0.6, 1.0), fancybox=True, shadow=False, fontsize= 8)
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
collist= ['S/N', 'OC/EC', ['EC', 'sulfate','OC','Ca'], ['nitrate', 'ammonia', 'chlorine', 'potassoium']]
plottypelist= ['line', 'bar','line', 'stack']
directions= ['L', 'L',['L','L','R', 'R'],['L','L','L','L']]
colors= ['r','g',['r', 'g','gold','navy'], ['b', 'gold', 'navy',  'tomato']]
multiplot(df,collist,plottypelist,directions,colors)

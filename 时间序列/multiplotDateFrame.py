#! /usr/bin/env python
# -*- conding: utf-8 -*-
#import matplotlib
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import matplotlib.dates as mdate
from matplotlib.dates import DateFormatter, DayLocator
font = {'family': 'serif',
        'color' : 'darkred',
        'weight': 'normal',
        'size'  : 8,
        }
axis_font = {'fontname':'Arial', 'size':'8'}
mpl.rcParams['legend.fontsize'] = 8
#mpl.rcParams['legend.loc'] = 'best'
mpl.rcParams['legend.handlelength'] = 0.7
def multiplot(df, collist, plottypelist, directions):
    axnum=len(collist)
    for i in range(axnum):
        ax = plt.subplot(axnum,1,i+1)
        if 'line' == plottypelist[i]:
                x=[collist[i][l] for l in range(len(directions[i])) if directions[i][l] == 'R']
                df1=df[collist[i]]
                if 'R' in directions[i]:
                    df1.plot(kind='line', ax=plt.gca(),  secondary_y=x, legend=True)#, fontsize=4)
                else:
                    if isinstance(collist[i],str):
                        df1.plot(kind='line', ax=plt.gca(), legend=True,title=collist[i])
                    else:
                        df1.plot(kind='line', ax=plt.gca(), legend=True)
                        ax.legend(loc='upper right', bbox_to_anchor=(0.5,0.95), ncol=2, fancybox=False, shadow=False)
                ax.get_xaxis().set_ticks([])
                ax.set_xlabel('')
        elif 'stack' == plottypelist[i] or 'bar' == plottypelist[i]:
            df1=df[collist[i]]
            ax=df1.plot(kind='bar',ax=plt.gca(),legend=True, stacked=plottypelist[i]=='stack')
            ax.set_xlabel('')
            if 'stack' == plottypelist[i]:
                ax.set_ylabel('Mass concentration (ug/m3)', fontdict = font)
               # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
                plt.grid()
                plt.legend(loc='upper center', bbox_to_anchor=(0.5,0.95), ncol=4, fancybox=True, shadow=False)
            else:
                plt.title(collist[i])
                ax.get_xaxis().set_ticks([])
                ax.set_xlabel('')
        else:
            print 'Type error!!\n'
    plt.show()
    return 0
if __name__=='__main__':
    df = pd.read_csv('sample.csv', parse_dates = True, index_col = 'datetime')
    collist= ['S/N', 'OC/EC', ['EC', 'sulfate','OC','Ca'], ['nitrate', 'ammonia', 'chlorine', 'potassoium']]
    plottypelist= ['line', 'bar','line', 'stack']
    directions= ['L', 'L',['L','R','L', 'R'],['L','L','L','L']]
    multiplot(df,collist,plottypelist,directions)

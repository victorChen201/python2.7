#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
from matplotlib.dates import DateFormatter,MonthLocator,DayLocator
from dateutil.parser import parse
import types
reload(sys)
sys.setdefaultencoding('utf-8')

def Averagedistantce(df, duration, sites, pollutants, types):
	'''
	'''
	df1 = dict()
	average = dict()
        averageSum=pd.Series(0, index=pollutants)
	for name in sites:
		temp = df[df['站点名称'.encode('gbk')].values==name.encode('gbk')][pollutants]
		df1[name] = temp.loc[duration[0]:duration[1],pollutants]
                df1[name] = df1[name].replace('—'.encode('gbk'),0)
		df1[name] = pd.DataFrame(df1[name].values.astype(np.float64),index=df1[name].index, columns=pollutants)
	        df1[name] = df1[name].resample('D').mean()
		average[name] = df1[name].mean()
                averageSum += average[name]
        #print averageSum
        for name in sites:
            if types == 'temporal':
                    df1[name] = df1[name] - averageSum/2
            else:
                    df1[name] = df1[name] - average[name]
        fig,ax=plt.subplots(len(sites)*len(pollutants),1 )
	index=0
	for name in sites:
		for pollutant in pollutants:
                        color_index = []
                        for x in df1[name][pollutant]:
                            if x>0:
                                color_index.append('r')
                            else:
                                color_index.append('b')
                        #ax1=df1[name].plot(x=df1[name].index, kind='bar', rot=90, ax=ax[index])
			ax[index].bar(df1[name].index, df1[name][pollutant], width=.5, color=color_index)
                        plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m'))
                        plt.gca().xaxis.set_major_locator(MonthLocator())
                        plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='left')
                        if index < len(sites)*len(pollutants)-1:
                            ax[index].get_xaxis().set_ticks([])
                        #ax[index].set_xlabel('')
                        ax[index].set_title(name,fontsize = 8)
                        ax[index].legend( [pollutant], loc = 'upper right', frameon = False, fontsize = 8)
                        #ax[index].grid(True, axis='both', linestyle = "-.")
                        index += 1

        fig.subplots_adjust(bottom=0.15)
        plt.grid()
	plt.show()
	return 0

df = pd.read_csv("2015.csv", parse_dates=True, index_col=u'时间'.encode('gbk'))
pollutants = ['CO', 'NO2', 'SO2']
duration = ['2015-01-01', '2015-12-30']
sites = [u'化工学校', u'高新区']
types = 'spatial' #'temporal'
Averagedistantce(df, duration, sites, pollutants, types)

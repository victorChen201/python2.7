#! /usr/bin/env python
# -*- coding: utf-8 -*-
#import matplotlib
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
from matplotlib.dates import DateFormatter, DayLocator, MonthLocator
#reload(sys)

from matplotlib.dates import DateFormatter, DayLocator
font = {'family': 'serif',
        'color' : 'darkred',
        'weight': 'normal',
        'size'  : 10,
        }
axis_font = {'fontname':'Arial', 'size':'8'}

def avaragedistance(df,duration,sites,pollutants,types):
    df1 = dict()
    avarage = dict()

    for name in sites:
        #df1[name] = df[df[u'站点名称']==name][duration[0]:duration[1],pollutants]
        df1[name] = df.loc[duration[0]:duration[1],pollutants]
        avarage[name] = df1[name].replace('',0).mean()
        df1[name] = df1[name] - avarage[name]
    fig,ax=plt.subplots(len(sites)*len(pollutants),1, figsize=(10,16))
    print df1
    index = 0
    for name in sites:
        for pollutant in pollutants:
            ax[index].bar(df1[name].index, df1[name][pollutant], alpha=0.4)
            ax[index].xaxis.set_major_formatter(DateFormatter('%Y-%m'))
            ax[index].xaxis.set_major_locator(MonthLocator())
            plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='left')
            index+=1
    plt.legend()
    plt.show()
    return 0

df = pd.read_csv('2013.csv', parse_dates=True, index_col='TimePoint', encoding='gbk')
#df = pd.read_csv('2015.csv', parse_dates = True, index_col = u'时间', encoding='gbk')
print df['CO']
pollutants= ['CO', 'SO2', 'NO2']
duration = ['2013-01-01', '2013-12-03']
sites = [u'化工学院']
types = 'spatial'# 'temporal'
avaragedistance(df,duration,sites,pollutants,types)

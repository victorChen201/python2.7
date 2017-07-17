#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import datetime
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
from matplotlib.dates import DateFormatter,MonthLocator,DayLocator
from dateutil.parser import parse
import types
reload(sys)
sys.setdefaultencoding('utf-8')

def Averagedistantce(df, duration, sites, pollutants, types, timelist):
        '''
        整点时间切片
        '''
        average = []
        for name in sites:
            averageSum = pd.DataFrame(columns=pollutants, index=timelist)
            temp=df[df['站点名称'.encode('gbk')]==name.encode('gbk')][pollutants]
            df1 = temp.loc[duration[0]:duration[1],pollutants]
            df1 = df1.replace('—'.encode('gbk'),0)
            df1 = pd.DataFrame(df1.values.astype(np.float64),index=df1.index, columns=pollutants)
            for i in timelist:
                dfhour=df1[df1.index.hour==i]
                    #for j in pollutants:
                averageSum.loc[i]=dfhour.mean()
            averageSum[name.encode('gbk')]=name.encode('gbk')
            average.append(averageSum)
            print averageSum
        return average

def Pollutantsthreshold(df,threshold):
    '''
    按阀值切片
    '''
    result = dict()
    for key,values in threshold:
        result[key] = df[df[key]>values]
    print result
    return result
df = pd.read_csv("2015_1_utf8.csv", parse_dates=True, index_col='datetime')
pollutants = ['CO', 'NO2', 'SO2']
duration = ['2015-01-01', '2015-12-30']
sites = ['化工学校', '高新区']
types = 'spatial' #'temporal'
timelist  = list(range(24))
df = df.replace('—',0)
stations = df['站点名称'] 
#print stations
df = df.drop('站点名称', axis=1)
df = pd.DataFrame(df.values.astype(np.float64),index=df.index, columns=df.columns)
df['站点名称'] = stations
#print df
df1 = df.groupby('站点名称').resample('D').mean
print df1
#diurnaldf=Averagedistantce(df, duration, sites, pollutants, types,timelist)
# for df1 in diurnaldf:

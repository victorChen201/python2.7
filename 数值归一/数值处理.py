#!/usr/bin/env python
# coding=utf-8
import numpy as np
import pandas as pd
import types
df = pd.read_csv("airpollutants2016.csv", parse_dates=True, index_col='TimePoint')



for i in df.columns:
    print i
    if i == 'PM2.5':
        prev=''
        last=''
        for j in df.index:
            print (df[i][j])
#print df.loc['2015-01-01 ']['PM10']
#print df
#df = df.loc[:,pollutants]
#df = df.replace('—'.encode('gbk'), 0)
#df=df.resample('D').mean()
#df=df[df['NO2']>=90]

#!/usr/bin/env python
# coding=utf-8
import numpy as np
import pandas as pd
import types
df = pd.read_csv("2015_1_utf8.csv", parse_dates=True, index_col='datetime')

df1 = df.groupby(df['站点名称'])
index = df.columns.delete(0)
gp = dict()
print index
for name,group in df1:
    gp[name] = group[index].replace('—',0).astype(np.float64) #替换－字符，并转换数据格式
    for j in gp[name].columns:
        if j == u'PM2_5':
            Continuous_invalid_value = 0
            for i in range(len(gp[name].index)):
                if i>0 and i<len(gp[name].index)-1:
                    if gp[name][j][i]>2*gp[name][j][i-1-Continuous_invalid_value] or gp[name][j][i]>2*gp[name][j][i+1]:
                        Continuous_invalid_value += 1
                        print name,j,i,gp[name][j][i]
                        gp[name][j][i] = np.nan
                    else:
                        Continuous_invalid_value = 0
                if gp[name][j][i]<0:
                    gp[name][j][i] = np.nan
                    print name,j,i
    gp[name] = gp[name].resample('D').mean()  #按天求平均值
#print df.loc['2015-01-01 ']['PM10']
#print df
#df = df.loc[:,pollutants]
#df = df.replace('—'.encode('gbk'), 0)
#df=df.resample('D').mean()
#df=df[df['NO2']>=90]

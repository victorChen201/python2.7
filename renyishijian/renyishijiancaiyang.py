#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("2013.csv",parse_dates=True, index_col='TimePoint', low_memory=False)

df=df.select_dtypes(include=['float64'])

columnnames=list(df)

df1=pd.DataFrame(columns=columnnames)

datetimedelta = pd.read_csv('datetimes.csv')

for i in range(len(datetimedelta)):
    data1=df[datetimedelta['Start'][i]:datetimedelta['End'][i]].mean()
    data1
    df1.loc[i] = data1

df1.insert(0, 'End', datetimedelta['End'])
df1.insert(0, 'Start', datetimedelta['Start'])
df1.to_csv('2013-specific.csv',index=True, encoding='utf-8')
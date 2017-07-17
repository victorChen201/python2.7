#!/usr/bin/env python
# coding=utf-8
import pandas as pd
import numpy as np
#统计时间段选择
period = ['2017-01-01','2017-04-02']
#列选择
columns = [u'Id', u'Project', u'Reporter', u'Assigned To', u'Category', u'OS',u'OS Version', u'Platform', u'Summary',u'Status', u'Resolution']

df = pd.read_csv('Estuary_Releases.csv', parse_dates=True, index_col='Date Submitted')

df = df[(df.index > period[0])&(df.index < period[1])]
df1 = dict(list(df[columns].groupby('Category')))
counts = df[columns].groupby('Category').count()
print counts
for key,values in df1.items():
    print '*********************************************************************'
    print key
    print values

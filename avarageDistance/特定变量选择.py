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
	'''
	
	average=[]
	for name in sites:
		print name.encode('gbk')
		df=df[df['站点名称'.encode('gbk')]==name.encode('gbk')][pollutants]
		if types=='seasonal':
			timeduration=[]
			timeduration.append(df[(df.index.month==3) | (df.index.month==4) | (df.index.month==5)])
			timeduration.append(df[(df.index.month==6) | (df.index.month==7) | (df.index.month==8)])
			timeduration.append(df[(df.index.month==9) | (df.index.month==10) | (df.index.month==11)])
			timeduration.append(df[(df.index.month==1) | (df.index.month==2) | (df.index.month==12)])
			lname=['spring','summer','autumn','winter']
		if types=='month':
			timeduration=[]
			df['month'] = df.index.dt.month
			lname = []
			[lname.append(i) for i in df['month'] if not i in lname]
			for l3 in lname:
				timeduration.append(df[(df.index.month==l3)])
		if types=='episode':
			timeduration=[]
			lname = []
			for i in range(len(duration)/2):
				timeduration.append(df[duration[i*2]:duration[i*2+1]])
				lname.append(duration[i*2])

		compoundindex=[]
		for x in lname:
			for y in range(len(timelist)):
				compoundindex.append(x)
		timeindex=timelist*len(lname)
		averageSum = pd.DataFrame(columns=pollutants, index=[compoundindex,timeindex])
		for ii in range(len(timeduration)):
			df1 = timeduration[ii]
			df1 = df1.replace('—'.encode('gbk'),0)
			df1 = pd.DataFrame(df1.values.astype(np.float64),index=df1.index, columns=pollutants)
			for i in timelist:
				dfhour=df1[df1.index.hour==i]
				for j in pollutants:
					# print j,lname[ii]
					# print dfhour.mean()
					# print lname[ii],i
					averageSum.loc[lname[ii],i][j]=dfhour.mean()[j]
					print averageSum.loc[lname[ii],i][j]
					# print averageSum.loc[lname[ii]][j][i],dfhour.mean()[j]

			# averageSum[name.encode('gbk')]=name.encode('gbk')
		average.append(averageSum)
			# print averageSum
	return average


df = pd.read_csv("2015_1.csv", parse_dates=True, index_col='datetime')
pollutants = ['CO', 'NO2', 'SO2']
:q
duration = ['2015-01-01','2015-03-30']
sites = ['化工学校','高新区'] #, '高新区'
types = 'seasonal' #'temporal'
timelist  = list(range(24))
#df = df.loc[:,pollutants]
df = df.replace('—'.encode('gbk'), 0)
df = pd.DataFrame(df.values.astype(np.float64),index=df.index, columns=pollutants)
df2=df.resample('D').mean()
df2=df2[df2['NO2']>=90]
# diurnaldf=Averagedistantce(df, duration, sites, pollutants, types,timelist)
# # for df1 in diurnaldf:
# diurnaldf[0].to_csv('tan.csv',index=True)
print df2  

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

def Averagedistantce(dff, duration, sites, pollutants, types, timelist):
	'''
	'''
	average=[]
	for name in sites:
		print dff
		df=dff[dff['站点'.encode('gbk')]==name.encode('gbk')][pollutants]
		if types=='seasonal':
			timeduration=[]
			timeduration.append(df[(df.index.month==3) | (df.index.month==4) | (df.index.month==5)])
			timeduration.append(df[(df.index.month==6) | (df.index.month==7) | (df.index.month==8)])
			timeduration.append(df[(df.index.month==9) | (df.index.month==10) | (df.index.month==11)])
			timeduration.append(df[(df.index.month==1) | (df.index.month==2) | (df.index.month==12)])
			lname=['spring','summer','autumn','winter']
		if types=='month':
			timeduration=[]
			df['month'] = df.index.month
			lname = []
			[lname.append(i) for i in df['month'] if not i in lname]
			for l3 in lname:
				timeduration.append(df[(df.index.month==l3)].drop('month', 1))
				print df[(df.index.month==l3)]
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
					averageSum.loc[lname[ii],i][j]=dfhour.mean()[j]

		average.append(averageSum)
	return average

df = pd.read_csv("airpollutants2016.csv", parse_dates=True, index_col='TimePoint')
pollutants = ['NO', 'NO2','NOx', 'SO2','O3','PM10','PM2.5'] #NO,NO2,NOx,SO2,O3,PM2.5,PM10
duration = ['2015-01-01','2015-03-30']
sites = ['故宫博物院'] #, '高新区'
types = 'seasonal' #'temporal'
timelist  = list(range(24))

df = df.replace('—'.encode('gbk'), 0)
df = pd.DataFrame(df,index=df.index, columns=pollutants)
df = pd.DataFrame(df.values.astype(np.float64),index=df.index, columns=pollutants)
df2=df.resample('D').mean()
df2=df2[df2['PM2.5']>=100]
dfindex=[]
for indexi in range(len(df2)): #creat a new datetimelist
	for houri in range(24):
		dfindex.append(df2.index[indexi] + pd.to_timedelta(houri, unit='h'))
df2index = pd.DatetimeIndex(dfindex)
print df2index
df=df.ix[df2index] #

df['站点'.encode('gbk')]='故宫博物院'.encode('gbk')
df3=pd.DataFrame(df,index=df.index)
diurnaldf=Averagedistantce(df3, duration, sites, pollutants, types,timelist)
for x in range(len(diurnaldf)):
	# diurnaldf[i].to_csv(sites[i].encode('gbk')+types+'diurnal.csv',index=True)
	df=diurnaldf[x]
	print df
	durations=list(df.index.levels[0])
	print durations
	print df.index.levels[1]
	for j in pollutants:
		for ii in durations:
			dftemp = df.loc[ii][j]
			dftemp.plot(kind='line', title=j)
		plt.legend(durations)
		plt.savefig(sites[x].encode('gbk')+types+j+' PM2.5 greater than diurnal.pdf')
		plt.close()
		# print list(df.get_level_values(0).unique())
	# df.plot(kind='line')


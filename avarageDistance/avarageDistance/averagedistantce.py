#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter,MonthLocator
from dateutil.parser import parse
import types
reload(sys)
sys.setdefaultencoding('utf-8')
def Averagedistantce(df, duration, sites, pollutants):
	'''
	'''
	print df
	df1 = dict()
	average = dict()
	for name in sites:
		#print 'station is %s' % name
		#print df['sites'].values[0].decode('gbk')
		
		temp = df[df['站点名称'.encode('gbk')].values==name.encode('gbk')][pollutants]
		df1[name] = temp.loc[duration[0]:duration[1],pollutants]
		df1[name] = pd.DataFrame(df1[name].values.astype(np.float64),index=df1[name].index, columns=pollutants)
		print df1[name]
		average[name] = df1[name].mean()
		print average[name]
		df1[name]= df1[name]- average[name]
		#print df1[name]
	fig,ax=plt.subplots(1,len(sites)*len(pollutants))
	index=0
	for name in sites:
		for pollutant in pollutants:
			ax[index].bar(index=df1[name].index, df1[name][pollutant], alpha = .2)
	plt.show()
	return 0

df = pd.read_csv("2015.csv", parse_dates=True, index_col=u'时间'.encode('gbk'))
df = df.replace('—'.encode('gbk'),0)
pollutants = ['CO', 'NO2', 'SO2']
duration = ['2015-01-01', '2015-01-02']
sites = [u'化工学校', u'高新区']
#df = pd.read_csv("2015.csv",parse_dates=True, usecols=pollutants, index_col=u'时间', encoding='gbk')	
Averagedistantce(df,duration,sites,pollutants)

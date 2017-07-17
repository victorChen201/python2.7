#!/usr/bin/env python
# -*- coding: utf-8 -*-
import seaborn
from matplotlib.patches import Rectangle
from dateutil.relativedelta import relativedelta
from matplotlib.ticker import FuncFormatter
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np
import matplotlib.cm as cm
from math import pi
import csv
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,MonthLocator,DayLocator, MONDAY
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.style 
import matplotlib


font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
axis_font = {'fontname':'Arial', 'size':'8'}

def timeseries(df,pollutants,directions,colors):
	ax1=[]
	axnum=len(pollutants)
	plt.style.use('classic')
	for i in range(axnum):
		ax = plt.subplot2grid((10*axnum,1), (i*10,0), rowspan=10)
		# ax.axhline(linewidth=0.4)
		# ax.axvline(linewidth=0.4)
		maxvalue=[]
		for j in range (len(pollutants[i])):
                        print df.index
                        print df[pollutants[i][j]]
			if directions[i][j]=='R':
				ax = ax.twinx()
				ax.plot(df.index, df[pollutants[i][j]],linewidth=0.4,color=colors[i][j])
				
				ax.spines['right'].set_color(colors[i][j])
				ax.tick_params(axis='y', colors=colors[i][j])
				ax.set_ylabel(pollutants[i][j], **axis_font)
				ax.yaxis.label.set_color(colors[i][j])

			else:
				ax.plot(df.index, df[pollutants[i][j]],linewidth=0.4,color=colors[i][j])
				ax.set_ylabel(pollutants[i][j], **axis_font)
			if i <axnum-1:
				ax.get_xaxis().set_ticks([])
				# ax.set_ylabel('')
			if i==axnum-1:
				alldays = MonthLocator() #DayLocator()              # minor ticks on the days
				dayFormatter = DateFormatter('%Y-%m') #DateFormatter('%b %d')      # e.g., 12
				ax.xaxis.set_major_locator(alldays)
				ax.xaxis.set_major_formatter(dayFormatter)
				plt.tick_params(labelsize=8) # The sise of tick label
				plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='left') #, horizontalalignment='right'
			maxvalue.append(max(df[pollutants[i][j]]))
			
			plt.tick_params(labelsize=8)
			plt.setp(ax.spines.values(), linewidth=0.4)
			plt.ylim(0,max(df[pollutants[i][j]]*1.1))
			if pollutants[i][j]=='Pressure':
				plt.ylim(970, max(df[pollutants[i][j]] ))
			if pollutants[i][j] == 'Temperature':
				plt.ylim(min(df[pollutants[i][j]])*1.05, max(df[pollutants[i][j]])*1.05)
			if i!=0:
				ax.spines['top'].set_visible(False)
			if directions[i][j]=='R':
				ax.legend( loc = (.75, .80), frameon = False, fontsize = 9)
			else:
				plt.legend(ncol = len(pollutants[i]),  frameon=False, fontsize = 9)
				#plt.legend(ncol=len(pollutants[i]), frameon=False)
				#plt.rc('legend', fontsize=9)


		ax1.append(ax)

	return ax1

df = pd.read_csv("airpollutants.csv",parse_dates=True, index_col='TimePoint')
# mpl.rcParams['legend.fontsize'] = 'large'
# pollutants=[['Temperature','Humidity'],['Visibility','WindS'],['NO2','NO','O3'],['SO2','CO'],['PM10','PM2.5']]
# directions=[['L','L'],['L','R'],['L','L','L'],['L','R'],['L','L'],['L','L'],['L','L']]
pollutants=[['Temperature','Humidity'],['WindS','Pressure'],['NO','NO2','NOx'],['SO2','O3'],['PM2.5','PM10']]
directions=[['L','R'],['L','R'],['L','L','L'],['L','R'],['L','L'],['L',' L']]
colors=[['g','b'],['gold','navy'],['b','r','g'],['greenyellow','deeppink','b'],['tomato','g'],['tomato','g'],['r','y'],['r','y'],['r','y']]
timeseries(df,pollutants,directions,colors)

plt.savefig('foshan.pdf') #, bbox_inches='tight'
plt.show()


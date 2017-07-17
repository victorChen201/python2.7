#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.dates import DateFormatter, DayLocator
import types
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

data = np.random.randint(1, 5, [3, 4])
print data
print data.shape
index = np.arange(data.shape[1])
print index
color_index = ['r', 'g', 'b']

#ax3 = plt.subplot2grid((20, 1),(0,0) ,rowspan=10)
fig,ax = plt.subplots(2,1, figsize = (10, 16))

#for i in range(data.shape[0]):
 #       ax1.bar(index + i*.25 + .1, data[i], width = .25, color = color_index[i],alpha = .5)
#for i in range(data.shape[0]):
 #       ax[0].bar(index + .25, data[i], width = .5, color = color_index[i],bottom = np.sum(data[:i], axis = 0), alpha = .7)
 #       ax3.bar(index + .25, data[i], width = .5, color = color_index[i],bottom = np.sum(data[:i], axis = 0), alpha = .7)
#ax3.barh(index, data[0], color = 'r', alpha = .5)
#ax3.barh(index, -data[1], color = 'b', alpha = .5)
#plt.yticks(np.arange(5),('Tom', 'Dick', 'Harri', 'Sally', 'Sue'))
#ax2.xaxis.set_major_locator(DateFormatter('%Y-%m'))
#ax2.xaxis.set_major_formatter(DayLocator())
#plt.tick_params(labelsize = 8)
#plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment= 'left')
#plt.setp(ax2.spines.values, linewidth=0.4)
plt.show()

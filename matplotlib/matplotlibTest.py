#!/usr/bin/python
#-*- coding:utf-8 -*-
from pylab import *
import numpy as np
figure(figsize=(8,6), dpi=80)
#figure(2)
ax1=plt.subplot(3,1,1)
#ax2=subplot(3,1,2)
#subplot(3,1,3)
x = np.arange(1,5)
plt.sca(ax1)
#plt.plot(x,x*2,label='Normal',c='blue')#指定每条线的label
plt.legend(loc='upper left')#显示图示,并指定图示的位置:best,upper right,upper lef,lower left,lower right,right,center left,center right,center right,lower center,upper center,center
plt.savefig('plot123.png') #保存文件
show()

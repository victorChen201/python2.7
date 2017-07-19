#!/usr/bin/env python
# coding=utf-8
import numpy as np
import pandas as pd
import types
import re
import chardet
nan = np.nan
debris = [u'-', ' ',u'—'.encode('gbk')]
def datenormalization(df, collist):
    dfloc = df[collist]
    #替换已知字符
    for i in debris:
        dfloc = dfloc.replace(i,np.nan)
    
    #查找非浮点数据类型
    for i in dfloc.columns:
        if dfloc[i].dtypes != np.float64:
            try:
                dfloc[i] = dfloc[i].astype(float)
            except:
                #print '%s列有非浮点数据类型'%i
                for j in range(len(dfloc.index)):
                    flag = 0
                    if dfloc[i][j]!=np.nan:
                        try:
                            float(dfloc[i][j])
                            flag = 1
                        except:
                            pass
                        finally:
                            if flag == 0:
                                print ('%s，第%s列不是整型或浮点型数据!'%(i,dfloc.index[j]))
    #排除负值，与平均值之差大于三倍标准差的值，如果是以小时统计的要排除大于２倍连续值的值
    for i in dfloc.columns:
        print i
        if dfloc[i].dtypes == np.float64:

            mean = dfloc[i].mean()
            std = dfloc[i].std()
            for j in range(len(dfloc.index)):
                if (dfloc[i][j] < 0):
                    print '数值%d为负数'%dfloc[i][j]
                    dfloc[i][j] = nan
                elif (dfloc[i][j] - mean) > 3*std:
                    print '%d大于３倍标准差'%dfloc[i][j]
                    dfloc[i][j] = nan
                elif (i == 'PM2.5') and (dfloc[i][j] != np.nan): 
                    if j>0 and j< (len(dfloc.index)-1) and (dfloc.index[j].day == dfloc.index[j].day) and (dfloc[i][j]>df[i][j-1]+dfloc[i][j+1]):
                        print '%d大于２倍周围值'%(dfloc[i][j])
                        dfloc[i][j]=nan
                else:
                    pass 
        else:
            pass
    return dfloc
if __name__=='__main__':
    collist =['NO','NO2','NOx','SO2','O3','PM2.5','PM10','WindD','WindS','Temperature','Humidity','Pressure','Precipitation']
    df = pd.read_csv("airpollutants2016.csv", parse_dates=True, index_col='TimePoint')
    
    df[collist] = datenormalization(df,collist)
    print df 
#print df.loc['2015-01-01 ']['PM10']
#print df
#df = df.loc[:,pollutants]
#df = df.replace('—'.encode('gbk'), 0)
#df=df.resample('D').mean()
#df=df[df['NO2']>=90]

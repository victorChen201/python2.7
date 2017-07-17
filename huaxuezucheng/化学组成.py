#! /usr/bin/env python
# -*- coding: utf-8 -*-
#import matplotlib
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.dates import DateFormatter, DayLocator
def mean_std(df):
    columnnames=list(df)
    df1=pd.DataFrame(columns=columnnames)

    spring=df[(df.index.month==3) | (df.index.month==4) | (df.index.month==5)]
    summer=df[(df.index.month==6) | (df.index.month==7) | (df.index.month==8)]
    autumn=df[(df.index.month==9) | (df.index.month==10) | (df.index.month==11)]
    winter=df[(df.index.month==1) | (df.index.month==2) | (df.index.month==12)]

    df1.loc[0]=spring.mean()
    df1.loc[1]=summer.mean()
    df1.loc[2]=autumn.mean()
    df1.loc[3]=winter.mean()

    df1.loc[4]=spring.std()
    df1.loc[5]=summer.std()
    df1.loc[6]=autumn.std()
    df1.loc[7]=winter.std()

    df2=pd.DataFrame(columns=columnnames)
    for i in range(len(columnnames)):    
        for j in range(4):
            df2.loc[j,columnnames[i]]=str(float('%.2f'%df1[columnnames[i]][j]))+'±'+str(float('%.2f'%df1[columnnames[i]][j+4]))
    return df2
if __name__=='__main__':

    df = pd.read_csv('airpollutants.csv', parse_dates = True, index_col = 'startdatetime')
    df=df.select_dtypes(include=['float64'])
    mean_std(df).to_csv("chemical compostion.csv",index=True)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("t2013.csv",parse_dates=True, index_col='TimePoint', low_memory=False)

df=df.select_dtypes(include=['float64'])
columnnames=list(df)
df1=pd.DataFrame(columns=columnnames)

spring=df[(3==df.index.month) | (df.index.month==4) | (df.index.month==5)]
summer=df[(df.index.month==6) | (df.index.month==7) | (df.index.month==8)]
autumn=df[(df.index.month==9) | (df.index.month==10) | (df.index.month==11)]
winter=df[(df.index.month==1) | (df.index.month==2) | (df.index.month==12)]

df1.loc[0]=spring.mean()
df1.loc[1]=summer.mean()
df1.loc[2]=autumn.mean()
df1.loc[3]=winter.mean()
ax=df1[['NO','NO2','NOx']].plot(kind='bar')
plt.show()

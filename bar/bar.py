import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123456)
import pandas as pd

# df = pd.DataFrame(3 * np.random.rand(4, 4), index=['a', 'b', 'c', 'd'],
#                   columns=['x', 'y','z','w'])

def align_labels(labels):
    for text in labels:
        x, y = text.get_position()
        h_align = 'left' if x > 0 else 'right'
        v_align = 'bottom' if y > 0 else 'top'
        text.set(ha=h_align, va=v_align)

df = pd.read_csv("airpollutants.csv",parse_dates=True, index_col='startdatetime')

df=df.select_dtypes(include=['float64'])

columnnames=list(df)
print columnnames
df1=pd.DataFrame(columns=columnnames)
spring=df[(df.index.month==3) | (df.index.month==4) | (df.index.month==5)]
summer=df[(df.index.month==6) | (df.index.month==7) | (df.index.month==8)]
autumn=df[(df.index.month==9) | (df.index.month==10) | (df.index.month==11)]
winter=df[(df.index.month==1) | (df.index.month==2) | (df.index.month==12)]

df1.loc[0]=spring.mean()
df1.loc[1]=summer.mean()
df1.loc[2]=autumn.mean()
df1.loc[3]=winter.mean()

plt.style.use('ggplot')
colors = plt.rcParams['axes.color_cycle']

list1=['OC','EC','sulfate','nitrate','ammonia','chlorine','potassoium','Ca','Na',"Mg"]
bar1list=list1[:] #OC ,EC, sulfate, nitrate, ammonia ,chlorine ,potassoium, cac

df=df1[bar1list]
df.index=['spring','summer','autumn','winter']
print type(df)
# df=df.T
# df.columns = ['spring','summer','autumn','winter']

# fig, axes = plt.subplots(nrows=2, ncols=2)
# for ax, col in zip(axes.flat, df.columns):
#     artists = ax.pie(df[col], autopct="%.1f%%", colors=colors, shadow=True,labels =bar1list)
#     ax.set(ylabel='', title=col, aspect='equal')
#     # align_labels(artists[-1])

ax=df[bar1list].plot(kind='bar', rot=360)
# fig.legend(artists[0], df.index, loc='center')
plt.savefig("seasonal-bar.pdf")
plt.show()

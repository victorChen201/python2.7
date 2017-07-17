
import numpy as np; np.random.seed(sum(map(ord, 'calmap')))
import pandas as pd
import calmap
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
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
from math import pi
import csv
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.style 
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
df = pd.read_csv("airpollutants.csv",parse_dates=True, index_col='TimePoint')


# events = pd.Series(df['OC'], index=df.index)
pollutants=['NO','NO2','SO2','O3','PM2.5']#['OC','EC','V','Pb']
fig, axes=calmap.calendarpollutants(df,pollutants=pollutants, year=2016, monthticks=1, daylabels='MTWTFSS',
                    dayticks=[0,1, 2,3, 4,5, 6], cmap='rainbow',
                    fillcolor='whitesmoke', linewidth=0,
                    fig_kws=dict(figsize=(20, 10)))
# axes[0].text(0.50, 0.75, 'left bottom',
#         horizontalalignment='left',
#         verticalalignment='bottom',
#         transform=axes[0].transAxes,fontdict=font)
# plt.title('Damped exponential decay', fontdict=font)
plt.show()



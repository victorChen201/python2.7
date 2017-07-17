#! /usr/bin/env python
# -*- conding:  utf-8 -*-
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

dates = ['01/02/1991', '01/03/1991', '01/04/1991']
xs = [datetime.strptime(d, '%m/%d/%Y').date() for d in dates]
ys = range(len(xs))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(xs, ys)
plt.gcf().autofmt_xdate()
plt.show()

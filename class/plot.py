#!/usr/bin/env python
# coding=utf-8
import  matplotlib.pyplot as plt
import  pandas as pd
import  numpy as np
import    pylab as mpl
from Tkinter import *
#from matplotlib.dates import DateFormater,MonthLocator,DayLoctor

__metaclass__= type
class plot(Frame):
    def __init__(self):
            Frame.__init__(self)
            self.main = self.master
            print 'hello plot',self.main
            mpl.rcParams['font.family'] = 'sans-serif'                                                           
            mpl.rcParams['font.sans-serif'] = ['SimHei']
            mpl.rcParams['axes.unicode_minus'] = False
    def plotbar(self, df):
            pass   
if __name__ == '__main__':
    a = plot()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-10 下午7:01
# @Author  : Leon
# @Site    : 
# @File    : demo13_根据日期分析股票涨幅.py
# @Software: PyCharm
import numpy as np
from datetime import *

#take:按照索引，从数组中提取索引对应的元素
#argmax:取数组中最大值对应的索引
#argmin:取数组中最小值对应的索引
'''
星期一:0
星期二:1
...
星期日:6
'''
def datestr2num(s):
    return datetime.strptime(s.decode('utf-8'),"%d-%m-%Y").date().weekday()

print(datestr2num(b'07-04-2011'))
dates,closeP = np.loadtxt('data.csv',delimiter=',',usecols=(1,6),unpack=True,converters={1:datestr2num})
print(dates)
dates = dates.astype(int)
print(dates)

averages = np.zeros(5)
for i in range(5):
    indexs = np.where(dates == i)
    prices = np.take(closeP,indexs)
    avg = np.mean(prices)
    print("Day",i,"prices",prices," 平均值:",avg)
    averages[i] = avg

top = np.max(averages)
print("最高平均收盘价:",top)
print("哪天收盘价最高:",np.argmax(averages))

bottom = np.min(averages)
print("最低平均收盘价:",bottom)
print("哪天收盘价最低:",np.argmin(averages))
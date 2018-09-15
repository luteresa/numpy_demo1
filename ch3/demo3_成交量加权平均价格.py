#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-8 上午10:41
# @Author  : Leon
# @Site    : 
# @File    : demo3_成交量加权平均价格.py
# @Software: PyCharm

from numpy import *
#代表金融资产的平均价格
#VWAP(Volume-Weighted Average Price)

#average()
price,volume=loadtxt('data.csv',delimiter=',',usecols=(6,7),unpack=True)
print(price)
print(volume)
vmap=average(price,weights=volume)
print('vmap=',vmap)

#mean()算数平均价格
m=mean(price)
print("mean=",m)

a=arange(100)
m=mean(a)
print(m)

#TWAP(Time-Weighted Average Price
#用一个依次增长的数列来模拟
t=arange(len(price))
print(t)
twap=average(price,weights=t)
print('twap=',twap)
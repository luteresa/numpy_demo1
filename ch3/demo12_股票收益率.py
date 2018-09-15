#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-8 上午11:50
# @Author  : Leon
# @Site    : 
# @File    : demo12_股票收益率.py
# @Software: PyCharm

import numpy as np

arr = np.loadtxt('data.csv',delimiter=',',usecols=(6,),unpack=True)
#1.简单收益率
#diff函数返回一个由相邻数组元素的差值构成的数组，类似于微积分中的微分。
#用差值除以前一天的价格
returns = np.diff(arr)
print(returns)
returns2 = returns/arr[:-1]
print(returns2)
print("标准差:",np.std(returns2))
#2.对数收益率：所有价格取对数后两两之间的差值；
#log(30)-log(20)=log(30/20)
logreturns = np.diff(np.log(arr))
print("对数收益率:",logreturns)

#std:计算标准差sqrt(((x1-a)^2+(x2-1)^2+...+(xn-a)^2)/n)
#where:可以根据设置的条件过滤数组中的值，返回相关项索引

print("简单收益率，正数:",np.where(returns2 >0)) #返回符合条件的项的索引
print("对数收益率（正数）:",np.where(logreturns>0))

#股票波动率:对价格变动的一种衡量
#年股票波动率:对数收益率的标准差除以对数收益率的平均值
annualVolatility = np.std(logreturns)/np.mean(logreturns)

print("年波动率：",annualVolatility/np.sqrt(1./252))

print("月波动率：",annualVolatility*np.sqrt(1./12))
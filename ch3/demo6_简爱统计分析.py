#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-8 上午11:39
# @Author  : Leon
# @Site    : 
# @File    : demo6_简爱统计分析.py
# @Software: PyCharm
import numpy as np

c=np.loadtxt('data.csv',delimiter=',',usecols=(6),unpack=True)

#中位数：median
print('price midean=',np.median(c))
sorted = np.msort(c)
n=len(sorted)
print('middle=',(sorted[n//2]+sorted[(n-1)//2])/2)

#方差:var
#假设数组元素算数平均数为a,元素位,x1,x2,x3...xn
#var=((x1-a)^2+(x2-1)^2+...+(xn-a)^2)/n
print('variance=',np.var(c))
print("variance from definition =", np.mean((c - c.mean())**2))
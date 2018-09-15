#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-8 上午11:18
# @Author  : Leon
# @Site    : 
# @File    : demo5_找最大小值.py
# @Software: PyCharm

from numpy import *
import numpy as np

#最值：max,min
h,l=loadtxt('data.csv',delimiter=',',usecols=(4,5),unpack=True)
print('highest price=',np.max(h))
print('lowest price=',np.min(l))

#极差值:数组取值范围ptp()
print('spread high price=',np.ptp(h))
print('spread low price=',np.ptp(l))
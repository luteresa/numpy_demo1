#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-21 上午11:54
# @Author  : Leon
# @Site    : 
# @File    : demo14_斐波那契数列.py
# @Software: PyCharm

import numpy as np

F = np.matrix([[1,1],[1,0]])
print("F:\n",F)

print("8th Fibonaci:",(F**7))

#Binet's Formula,黄金分割公式
n = np.arange(1,9)
sqrt5 = np.sqrt(5)
phi = (1+sqrt5)/2
fibonacci = np.rint((phi**n - (-1/phi)**n)/sqrt5)
print("Fibonaci:",fibonacci)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午8:22
# @Author  : Leon
# @Site    : 
# @File    : demo17_方波.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import sys

'''
方波：
方波可以表示无穷的傅里叶级数
'''
t = np.linspace(-np.pi, np.pi, 201)

k = np.arange(1,float(sys.argv[1]))
k =  2*k -1

f = np.zeros_like(t)

for i in range(len(t)):
    f[i] = np.sum(np.sin(k*t[i])/k)
f = (4/np.pi) * f

plt.plot(t,f)
plt.show()




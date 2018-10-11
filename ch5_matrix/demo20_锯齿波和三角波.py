#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午8:32
# @Author  : Leon
# @Site    : 
# @File    : demo20_锯齿波和三角波.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import sys

t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1,float(sys.argv[1]))
f = np.zeros_like(t)

for i in range(len(t)):
    f[i] = np.sum(np.sin(2*np.pi*k*t[i])/k)

f = (-2/np.pi)*f

plt.plot(t,f,lw=1.1)
plt.plot(t,np.abs(f),lw=2.0)
plt.show()
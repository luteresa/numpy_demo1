#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-10-9 下午8:12
# @Author  : Leon
# @Site    : 
# @File    : demo15_利萨茹曲线.py
# @Software: PyCharm
import numpy as np
import sys
import matplotlib.pyplot as plt
'''
利萨茹曲线的参数包括A 、B、a和b。为简单起见,我们令A和B均为1。
(1) 使用linspace函数初始化变量t ,即从-pi到pi上均匀分布的201个点:

'''
a = float(sys.argv[1])
b = float(sys.argv[2])

a = 9
b = 8
t = np.linspace(-np.pi, np.pi, 201)

x = np.sin(a*t + np.pi/2)
y = np.sin(b * t)

plt.plot(x,y)
plt.show()
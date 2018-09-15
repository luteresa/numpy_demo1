#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-7 下午7:38
# @Author  : Leon
# @Site    : 
# @File    : demo1_csv文件.py
# @Software: PyCharm
import numpy as np
#创建一个单位矩阵
i2 = np.eye(2)
print(i2)
np.savetxt("eye.txt",i2)

a=np.arange(20)
print(a)

np.savetxt("a.txt",a,fmt='%d')
np.savetxt("b.txt",a,fmt='%.2f')

aa=np.loadtxt("a.txt",dtype='int')
print(aa)
bb=np.loadtxt("b.txt",dtype='float')
print(bb)

x=np.arange(16).reshape(4,4)
print(x)
np.savetxt("x.txt",x,fmt='%d')

y=np.loadtxt('x.txt',dtype='int')
print(y)
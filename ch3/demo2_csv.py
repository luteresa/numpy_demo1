#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-7 下午8:28
# @Author  : Leon
# @Site    : 
# @File    : demo2_csv.py
# @Software: PyCharm

from numpy import *
#通过逗号分隔符读写文本文件

#savetxt,loadtxt
a=arange(20).reshape(4,5)
print(a)
savetxt('a.txt',a,fmt='%d',delimiter=',')


b=loadtxt('a.txt',dtype='int',delimiter=',',usecols=(1,3,4))
print(b)

x,y=loadtxt('x.txt',delimiter=',',dtype='float',usecols=(1,2),unpack=True)
print(x)
print(y)

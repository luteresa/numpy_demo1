#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-10 下午8:59
# @Author  : Leon
# @Site    : 
# @File    : demo14_数组的修剪和压缩.py
# @Software: PyCharm
from numpy import *
'''
clip compress
数组的修剪：将所有比给定最大值还大的元素，都设定为给定最大值
所有比给定最小值还小的数组值设定为指定的最小值
'''

a = arange(10)
print('a:',a)
print('clipped',a.clip(min=3,max=8))

#a: [0 1 2 3 4 5 6 7 8 9]
#clipped [3 3 3 3 4 5 6 6 6 6]

#压缩：返回数组中所有满足条件元素，组成一个可能比元素组小的数组
print('compressed',a.compress(a > 5))
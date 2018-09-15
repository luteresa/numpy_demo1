#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-7 下午5:50
# @Author  : Leon
# @Site    : 
# @File    : demo5_数组的分割.py
# @Software: PyCharm
import numpy as np
from numpy import *

def print_line():
    print("==="*20)
a = arange(9).reshape(3,3)
print(a)

#1.水平分割
b=hsplit(a,3)
for item in b:
    print(item)
print_line()

c=split(a,3,axis=1)
print(type(c))
for item in c:
    print(item)
print_line()

#2.垂直分割
b=vsplit(a,3)
for item in b:
    print(item)
c=split(a,3,axis=0)
for item in c:
    print(item)
print_line()

#3.深度分割
#按深度方向，切蛋糕,切完之后维度是(3,3,1)
c=arange(27).reshape(3,3,3)
print(c)
d=dsplit(c,3)
print(type(d))
for item in d:
    print(item.shape)

print_line()

print(c.ndim)

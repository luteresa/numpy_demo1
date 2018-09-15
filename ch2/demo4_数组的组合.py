#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-7 下午5:29
# @Author  : Leon
# @Site    : 
# @File    : demo4_数组的组合.py
# @Software: PyCharm
import numpy as np
from numpy import *

def print_line():
    print("==="*20)
a = arange(9).reshape(3,3)
b=2*a
print(a)
print(b)
print_line()

#1.水平组合
print(hstack((a,b)))
print(concatenate((a,b),axis=1))
print_line()

#2.垂直组合
print(vstack((a,b)))
print(concatenate((a,b),axis=0))
print_line()

#3.深度组合：沿“深度”进行叠加
print(dstack((a,b)))

#4.列组合：
#对于一维数组，按列方向进行组合
oned=arange(2)
twice_ond=oned*2
print(column_stack((oned,twice_ond)))
#[[0 0]
 #[1 2]]
 #对于多维数组，功能同hstack()

#5.行组合
#对于一维数组，按行方向进行组合
print(row_stack((oned,twice_ond)))
#[[0 1]
#[0 2]]
#对于多维数组，功能同vstack()
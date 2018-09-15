#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-7 下午7:13
# @Author  : Leon
# @Site    : 
# @File    : demo6_数组的属性.py
# @Software: PyCharm
import numpy as np
from numpy import *
b=arange(24).reshape(2,12)

#1.ndim数组维度
print(b.ndim)

#2.size：数组元素总数
print(b.size)

#3.itemsize:数组中单个元素所占内存字节数
print(b.itemsize)

#4.nbytes:size*itemsize
#整个数组所占存储空间
print(b.nbytes)

#5.T 等效于transpose
b.resize(6,4)
print(b)
print(b.T)
#对于一维数组,.T就是其本身
a=arange(6)
print(a.T)

#6.复数
c=array([1.j+1,2.j+3])
print(c)
print(c.real)
print(c.imag)
print(c.dtype)

#7.flat:迭代器
#是唯一获得flatiter对象的方式，可以像遍历一维数组一样去遍历多维数组
b=arange(4).reshape(2,2)
print(b)
f = b.flat
for item in f:
    print(item)
#可以用flatiter直接获取一个数组元素
print(b.flat[2])
print("*"*20)
#可以获取多个元素
print(b.flat[[1,3]])

#flat属性可以被赋值,对flat属性赋值将导致整个数组元素都被覆盖
b.flat=8
print(b)
#对指定flat赋值，改变相对应元素
b.flat[[1,2]]=2
print(b)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-7 下午4:47
# @Author  : Leon
# @Site    : 
# @File    : 改变数组的维度.py
# @Software: PyCharm
import numpy as np
from numpy import *

def print_line():
    print("==="*20)
#1.reshape函数，变为多维
b=arange(24).reshape(4,6)
print(b)
print_line()

#2.ravel展平数组,返回一个视图
c=b.ravel()
print(c)
print(b)
print_line()

#3.flatten
#功能同ravel，不过会实际分配内存来保存结果，ravel只是展开一个视图
c=b.flatten()
print(c)
print(b)
print_line()

#4.用元组设置维度,同reshape()，直接改变数组
b.shape=(3,8)
print(b)
print_line()

#5.transpose在线性代数中常用的转置矩阵
d=b.transpose()
print(d)

#5.resize:和reshape功能一样，但是resize直接改变数组本身
b.resize((2,12))
print(b)
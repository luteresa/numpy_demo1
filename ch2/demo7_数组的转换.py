#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-7 下午7:31
# @Author  : Leon
# @Site    : 
# @File    : demo7_数组的转换.py
# @Software: PyCharm
import numpy as np
from numpy import *

b=array([1.+1.j,3.+3.j])
print(b)
#[1.+1.j 3.+3.j]

#tolist:将Numpy数组转换成Python列表
print(b.tolist())
#[(1+1j), (3+3j)]
print("*"*88)
#astype:转换数组时指定数据类型
print(b.astype(int))  #丢掉虚数部分
print(b.astype('complex'))  #可以字符串做参数
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-7 下午4:13
# @Author  : Leon
# @Site    : 
# @File    : array1.py
# @Software: PyCharm

import numpy as np
from numpy import *
a=arange(9)
print(a)
#数组切片，类似于序列操作
print(a[3:7])
print(a[:7:2])
print(a[::-1]) #逆序
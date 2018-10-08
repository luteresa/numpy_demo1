#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-21 上午11:48
# @Author  : Leon
# @Site    : 
# @File    : demo11_模运算.py
# @Software: PyCharm

import numpy as np

'''
计算模数或者余数，可以使用NumPy中的mod,remainder和fmod函数
'''

#remainder：逐个返回两个数组中元素相除后的余数
a = np.arange(-4,4)
print("remainder:",np.remainder(a,2))
#mod:同remainder
print("mod:",np.mod(a,2))

#‘%’remainder的缩写
print("%:",a%2)

#fmod：处理负数与(remainder,mod)不同，所得余数正负与被除数一致
print("fmod:",np.fmod(a,2))
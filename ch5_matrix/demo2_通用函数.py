#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-30 下午4:22
# @Author  : Leon
# @Site    : 
# @File    : demo2_通用函数.py
# @Software: PyCharm

import numpy as np
import cv2
import caffe
#通用函数的输入是一组标量,输出也是一组标量,它们通常可以对应于基本数学运算,如加、减、乘、除等。

def ultimate_answer(a):
    result = np.zeros_like(a)
    result.flat = 42
    return  result

ufunc=np.frompyfunc(ultimate_answer,1,1)
print('The answer',ufunc(np.arange(4)))
print('The answer',ufunc(np.arange(4).reshape(2,2)))

'''
其实通用函数并非真正的函数,而是能够表示函数的对象。
通用函数有四个方法,不过这些方法只对输入两个参数、输出一个参数的ufunc对象有效,
例如add函数。其他不符合条件的ufunc对象调用这些方法时将抛出 ValueError异常。因此只能
在二元通用函数上调用这些方法。以下将逐一介绍这4个方法:
reduce
accumulate
reduceat
outer
1
'''
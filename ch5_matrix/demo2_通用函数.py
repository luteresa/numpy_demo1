#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-30 下午4:22
# @Author  : Leon
# @Site    : 
# @File    : demo2_通用函数.py
# @Software: PyCharm

import numpy as np
#通过NumPy的frompyfunc函数来创建通用函数
#通用函数的输入是一组标量,输出也是一组标量,它们通常可以对应于基本数学运算,如加、减、乘、除等。

def ultimate_answer(a):
    result = np.zeros_like(a) #创建一个形状和a类似，值为0的数组
    result.flat = 42
    return  result

ufunc=np.frompyfunc(ultimate_answer,1,1)
print('The answer:',ufunc(np.arange(4)))
#可以对二位数组进行完全一样的操作
print('The answer:',ufunc(np.arange(4).reshape(2,2)))

'''
其实通用函数并非真正的函数,而是能够表示函数的对象。
通用函数有四个方法,不过这些方法只对输入两个参数、输出一个参数的ufunc对象有效,
例如add函数。其他不符合条件的ufunc对象调用这些方法时将抛出 ValueError异常。因此只能
在二元通用函数上调用这些方法。以下将逐一介绍这4个方法:
'''

'''reduce:
沿指定的轴，在连续的数组元素之间递归调用通用函数，
对于add，其效果等价于对数组求和
'''
a = np.arange(9)
print(a)
print("reduce",np.add.reduce(a))

'''
accumulate:
同reduce，在连续的数组元素之间递归调用通用函数，
但是会存储运算的中间结果,add上调用accumulate,等价于cumsum函数
'''
print("accumulate",np.add.accumulate(a))
print("multipyle:",np.multiply.accumulate([2,3,5]))


'''
reduceat:
传入一个数组，以及一个索引值列表作参数
[0,5,2,7]相当于 
np.add.reduce(a[0:5])
np.add.reduce(a[5:2])
np.add.reduce(a[2:7])
np.add.reduce(a[7:])
'''
print("accumulate",np.add.reduceat(a,[0,5,2,7]))

'''
outer:rank = rank(a1) + rank(a2)
'''

print("outer:\n",np.add.outer(np.arange(3),a))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-30 下午5:07
# @Author  : Leon
# @Site    : 
# @File    : demo3_add调用通用函数.py
# @Software: PyCharm

import numpy as np

a=np.arange(9)
print('Reduce',np.add.reduce(a))
print("Accumulate",np.add.accumulate(a))

print("reduceat",np.add.reduceat(a,[0,5,2,7]))
#outer返回一个数组，它的秩等于两个输入的秩的和
print("Outer ",np.add.outer(np.arange(3),a))
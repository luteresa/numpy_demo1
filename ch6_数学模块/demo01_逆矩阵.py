#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-10-11 下午5:50
# @Author  : Leon
# @Site    : 
# @File    : demo01_逆矩阵.py
# @Software: PyCharm

import numpy as np
#使用mat函数创建示例矩阵:
A = np.mat("0 1 2;1 0 3;4 -3 8;1 2 3")
print(A)

#inv函数计算逆矩阵,如果输入是奇异矩阵或非方阵，则抛出异常
try:
    inverse = np.linalg.inv(A)
    print(inverse)
    ret = True
except Exception as e:
    print("--------------error-------------")
    print(e)
    ret = False

if ret==True:
    print("Check:\n",A*inverse)
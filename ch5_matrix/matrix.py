#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-30 下午4:07
# @Author  : Leon
# @Site    : 
# @File    : matrix.py
# @Software: PyCharm

import numpy as np

#1.mat函数使用字符串创建矩阵
A = np.mat('1 2 3;4 5 6;7 8 9')
print('A:')
print(A)
#T属性获取矩阵的转置
print('transpose A:')
print(A.T)
#I属性获得矩阵的逆
print('Inverse A:')
print(A.I)
#mat函数，若输入已为matrix或ndarray对象，则不会创建副本，这是用mat
#和调用matrix(data,copy=False)等价

print('*'*88)
#2.从已有矩阵创建新的矩阵
#有时需要用较小的矩阵来创建较大矩阵，用bmat实现

#创建2x2单位矩阵
B=np.eye(2)
print(B)
#创建通型矩阵，乘以2
C=2*B
print(C)

#使用字符串创建符合矩阵，格式于mat类似
print('Compound matrix:\n',np.bmat("B C;B C"))

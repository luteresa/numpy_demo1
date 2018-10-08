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
#mat函数，若输入已为matrix或ndarray对象，则不会创建副本，这时用mat
#和调用matrix(data,copy=False)等价

#2.除了使用字符串创建矩阵以外, 我们还可以使用NumPy数组进行创建:
B=np.mat(np.arange(9).reshape(3,3))
print("B",B)

print('*'*88)
#2.从已有矩阵创建新的矩阵
#有时需要用较小的矩阵来创建较大矩阵，用bmat实现(block matrix)

#创建2x2单位矩阵
C=np.eye(2)
print("C:",C)
#创建通型矩阵，乘以2
D=2*C
print("D:",D)

#使用字符串创建复合矩阵，格式与mat类似
print('Compound matrix:\n',np.bmat("C D;C D"))

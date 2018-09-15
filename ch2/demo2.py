#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-18 上午11:49
# @Author  : Leon
# @Site    : 
# @File    : demo2.py
# @Software: PyCharm
from numpy import *
#改变数组维度
b = arange(24).reshape(2,3,4)
print(b)
#访问单个数组元素
print(b[1,1,1])
#第一维度所有的[1,1]位置的元素
print(b[:,1,1])
#第一维度所有元素
print(b[0])
print(b[0,:,:])  #等价于b[0]
print(b[0,...]) #等价于b[0],多个":"可以用"..."代替
#可以在数组任意维度中,做一维数组支持的切片
#把三维数组看作多个楼层，多个行，多个列的房间号分布
print("*"*88)
print(b[0,1,::2]) #第0层，第1行，列每隔2选一个
print(b[...,2])   #所有楼层，所有行，第2列的房间号
print(b[0,:,-1])   #第一层，最后一列所有房间
print("*"*88)
print(b[0,::-1,-1])   #第一层，最后一列所有房间反向选取

#如果多维数组中执行翻转一维数组的命令，将在第一维度上翻转所有元素
print(b[::-1])
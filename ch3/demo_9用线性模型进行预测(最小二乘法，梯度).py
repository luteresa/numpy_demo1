#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-10 下午8:15
# @Author  : Leon
# @Site    : 
# @File    : demo_9用线性模型进行预测(最小二乘法，梯度).py
# @Software: PyCharm
import numpy as np
#线性模型：直线方程f(x), f(x1,x2), 预测就是根据x求对应的y

#问题变成了求直线方程
'''
提供一组离散点，通过数学公式，计算出总体上最接近这些离散点的直线
通过直线就会得到一个直线方程
（1,6）
（2,5）
（3,7）
（4,10）
（5,?）
y=b1*x + b2

6=b1*1 + b2
5=b1*2 + b2
7=b1*3 + b2
10=b1*4 + b2

f(b1,b2) = (6-(b1*1 + b2))^2 + (5-(b1*2 + b2))^2
            + (7-(b1*3 + b2))^2+(10-(b1*4 + b2))^2
求f(b1,b2)最小值,min(f(b1,b2))

d(f(x))/d(x)=0

二元函数，求偏导数
d(f(b1,b2))/d(b1)=0
d(f(b1,b2))/d(b2)=0

d(f(b1,b2))/d(b1) = 20b1 + 8b2 - 16 = 0
d(f(b1,b2))/d(b2) = 60b1 + 20b2 -154 = 0
b1 = 1.4
b2 = 3.5

==>y=1.4*x + 3.5
f(5) = 1.4*5 + 3.5 = 10.5

lstsq:返回线性矩阵方程的最小二乘法的解
'''
x = np.array([1,2,3,4])
y = np.array([6,5,7,10])
a = np.vstack([x,np.ones(len(x))]).T
print(a)
b1,b2 = np.linalg.lstsq(a,y)[0]
print(b1, b2)


from matplotlib.pyplot import *
plot(x,y,'o',label='Point',markersize=15)
plot(x,b1*x+b2,'b',label='Fitter Line')
legend()
show()

a = np.array([3,4])
b = np.array([2,3])
print(np.dot(a,b))
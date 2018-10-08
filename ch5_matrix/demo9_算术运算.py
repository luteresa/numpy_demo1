#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-19 下午8:23
# @Author  : Leon
# @Site    : 
# @File    : demo9_算术运算.py
# @Software: PyCharm

'''


在NumPy中,基本算术运算符+、-和*隐式关联着通用函数add、subtract和multiply。
也就是说,当你对NumPy数组使用这些算术运算符时,对应的通用函数将自动被调用。
除法包含的过程则较为复杂,在数组的除法运算中涉及三个通用函数divide、true_divide和floor_division,
以及两个对应的运算符/和//
'''

import numpy as np

#divide
a = np.array([2,6,5])
b = np.array([1,2,3])
print(np.divide(a,b),np.divide(b,a))

#true_divide
print(np.true_divide(a,b),np.true_divide(b,a))

#floor_divide:向下取整
print(np.floor_divide(a,b),np.floor_divide(b,a))

#'/'==true_divide
print("/ operator:\n",a/b,b/a)
#'//'==floor_divide
print("// operator:\n",a//b,b//a)


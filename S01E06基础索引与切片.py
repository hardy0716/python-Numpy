# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 09:08:30 2022

@author: 15517
"""
import numpy as np
a = np.arange(10)
A = np.arange(20).reshape(4,5)

# 一维数组
# 语法： 序列[开始位置下标:结束位置下标:步长]

print(a[3],a[5],a[-1])  # 3 5 9
print(a[2:4])           # array([2 3])
print(a[2:8:2])         # array([2,4,6])

# 二维数组  #索引行列坐标，类似EXCEl
print(A)
print(A[0,0])           # 0行0列位置  0
print(A[-1,2])          # 最后一行第二列  17  
print(A[2])             # 第二行  [10 11 12 13 14]
print(A[-1])            #最后一行 [15 16 17 18 19]
print(A[0:-2])          #除了最后两行
print(A[0:2,2:4])       #第0、1两行的第2、3两列的四个数
print(A[:,2])           #第2列所有数

# 切片修改  （会改变原来的数组）
print(a)
a[4:6] = 520    #第4、5位置的数值修改为520
print(a)

A[:1,:2] = 520  #第0行的第0、1列修改为520
print(A)























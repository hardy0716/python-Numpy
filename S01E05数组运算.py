# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 22:17:51 2022

@author: 15517
"""
#1.3.1 reshape不改变值修改形状
import numpy as np
import random


a = np.arange(10).reshape(2,5)  # 变成2行5列
b = a.reshape(10)               # 变回1行1列
c = a.flatten()                 # 不清楚对方什么阵型，直接转一维
print(b)

d = a.reshape(1,10)
e = a.reshape(10)

#a.flatten()    作用：将一个多维数组展开变成一个一维数组

# shape：返回数组的维度
# reshape:不改变数组的值，修改形状
print(a.shape)

#1.3.2数组运算
print(a)
x = a + 1                   #所有元素都加1
print(x)  
print(a*3)                  #所有元素均乘3

#凡是形状一样的数组，假设数组a和数组b，可以直接用a+b 或 a-b
a = np.arange(10).reshape(2,5)
b = np.random.randn(2,5)    #2行5列的随机数
print(a+b)
print(a-b)

#注：如果分母为0，0/0返回nan，其它数/0返回inf
# nan = Not a Number 不是一个数字
a = np.arange(6)
b = np.arange(24).reshape(4,6)
print(a)
print(b)
print(b-a)  #可以计算， a为1行6列，b为4行6列，则b的每一行都减去a的每一行

a = np.array([
    [3,4,5,7,2],
    [2,5,3,5,4]]
    )
b = np.array([2,1,3,2,2])
print(a-b)
print(a*b)


a = np.array([
    [3,5,7,6,4],
    [2,3,5,3,4],
    [5,6,7,3,9],
    [4,5,2,1,3],
    [6,7,6,9,4]])
b = np.array([
    [3],
    [2],
    [3],
    [1],
    [3]])

print(a-b)
print(a+b)



#1.3.3 广播规则
a = np.arange(18).reshape(3,2,3)   #(3,2,3)3块 2行3列的数组
b = np.random.randn(2,3)           #(2,3) 二维 2行3列的数组
print(b.shape)
print(a+b)                         #可以运算

c = np.arange(3)
print(c.shape)                     #(3,) 一维有3个元素的数组 
print(a+c)                         # 可以运算                 

d = np.random.randn(2,1)
print(d.shape)                     #(2,1) 二维 2行1列的数组
print(a+d)                         #可以运算

e = np.random.randn(2,4)
print(e.shape)                     #(2,4) 二维 2行4列的数组
print(a+e)                         # 不可以运算


#广播主要发生在两种情况，一种是两个数组的维数不相等，但是它们的后缘维度的轴长相符，
#另外一种是有一方的长度为1。













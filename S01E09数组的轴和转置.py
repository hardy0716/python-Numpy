# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 13:35:14 2022

@author: 15517
"""

import numpy as np
数组=np.array([
    [[1,2],[4,5],[7,8]],
    [[8,9],[11,12],[14,15]],
    [[10,11],[13,14],[16,17]],
    [[19,20],[22,23],[25,26]]
             ])
print(数组.shape)  # 返回 (4, 3, 2)
print(数组)
#数组的shape维度是（4,3,2），元组的索引为 [ 0,1,2 ]
# 0轴是行，1轴是列，2轴是纵深
# 凡是提到轴，先看数组的维度，有几维就有几个轴

# 2.1 沿轴切片
a=np.array([  [1,2,3] , [4,5,6] , [7,8,9]  ])
print(a)
print(a.shape)  #(3,3)   元组索引为[0,1] 0轴式行，1轴式列

# 一个参数的切片
print(a[:2])    #切a的0、1两行  ~ 0轴的0、1两行
# 两个参数的切片
print(a[:2,1:])  #切a的0、1两行和1、2两列的交集； ~ 0轴的0、1行，1轴的1，2行

# 2.2 传入轴编号
b = np.arange(16).reshape(2,2,4)
print(b)
print(b.shape)



# 三、numpy数组转置换轴
data = np.array([
    [1,2],
    [3,4],
    [5,6]
    ])
print(data)
print(data.T)                #转置 data.T
# 可以使用reshape
print(data.reshape(2,3))     #会与data.T 有差异

data1 = np.arange(1,7)
print(data1)
print(data1.T)

print(data1.reshape(2,3))
print(data1.reshape(3,2))


# 3.1transpose方法 行列转置
x = np.arange(24).reshape(4,6)
print(x)
print(x.transpose())


# 3.2 swapaxes方法 轴转置
print(x)
print(x.swapaxes(1,0))   #0轴和1轴互换



# 轴转置心得
# 三维数组在进行轴转置时， 不变的维的数据 不动
arr = np.arange(16).reshape(2,2,4)  # 2块，2行4列的数组
print(arr)
arr.transpose((1,0,2))          #块和行转置，shape为（2，2，4） ，
# 列的顺序不变，行和块之间进行变换
arr.transpose((2,1,0))          #块和列转置，shape为（4,2,2）
# 行的顺序不变，列和块之间进行变换  
arr.transpose(0,2,1)            #行和列转置，shape为(2,4,2)

# swapaxes和transpose 没什么太大的区别
# transpose( *, *,*)  有三个参数 初始为(0,1,2) 
# swapaxes(*, *) 有两个参数
arr.transpose(1,0,2)  # 0 和 1 互换
arr.swapaxes(1,0)    # 0 和 1 互换
#  即 arr.transpose(1,0,2) = arr.swapaxes(1,0) 




















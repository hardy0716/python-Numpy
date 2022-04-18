# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 09:48:04 2022

@author: 15517
"""
# 布尔值  Ture False
#一维数据
import numpy as np
a = np.arange(6)
print(a)
fil = a > 3
print(fil)           #[False False False False  True  True]
print(a[fil])        #[4 5]

# 实例1 ： 吧一维数组进行01化处理
a[a < 3] = 0
a[a >= 3] = 1
print(a)             #[0 0 0 1 1 1]

# 实例2：进行自增量的操作，给大于3的数加上520
a[a > 3] += 520  #  a[a > 3] = a[a > 3] + 520
print(a)


# 二维数组
b = np.arange(1,21).reshape(4,5)
print(b)
fil2 = b > 10           #布尔值
print(fil2)             # 返回一个布尔数组，即有行又有列
print(b[fil2])          # 返回所有为True的对应数字组成的数组，以一维数组展现

# 例：把第3列大于5的行筛选出来并重新赋值为520
fil3 = b[:,3] > 5
print(fil3)         #[False  True  True  True]  第3列中的1、2、3行大于5
b[:,3][fil3] = 520
print(b)


数组 = np.array([[10,20,30],[50,40,10],[10,1,10]])
print(数组)
筛选 = 数组>25
print(筛选)
print(数组[筛选])



#条件组合：找出偶数或小于7的数
c = np.arange(10)
print(c)
print('-'*30)
condition = (c%2 ==0) | (c < 7)
print(condition)
print('-'*30)
print(c[condition])




































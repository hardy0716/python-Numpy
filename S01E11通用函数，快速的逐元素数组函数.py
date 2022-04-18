# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:51:53 2022

@author: 15517
"""

# 六、通用函数：快速的逐元素数组函数
# 通用函数也可以称为 ufunc， 是一种在 ndarray 数据中进行逐元素操作的函数。
import numpy as np
# 一元ufunc  通用函数
a = np.arange(10)
print(a)
print(np.sqrt(a))   #返回正值的平方根  ~ print(a**0.5)
print(np.exp(a))    #计算每个元素的自然指数值e的x次方

#二元通用函数：比如 add 和 maximum 则会接受两个数组并返回一个数组结尾结果，所以叫做二元通用函数。
x = np.random.randn(8)    # randn从标准正态分布中得到的随机变量
y = np.random.randn(8)
print(x)
print(y)
print(np.maximum(x,y))   # 对位比较大小，取大的，生成新的数组返回，逐个元素地将 x和 y 中元素的最大值计算出来

# 还要好多函数 自己总结！！！！！！！！！！！！！
print(np.sign(x))        # 计算各元素的正负号， 1：正； -1：负； 0： 零
# ceil 天花板  floor 地板  rint 四舍五入到整数
print(np.modf(x))        # modf 将数组中数据的小数位和整数位两部分独立写开
print(np.mod(5,4))       # mod(除数，被除数)  返回余


# 7.1 数学和统计方法
# prod 乘积；  argmin,argmax 最小和最大值的位置
# cumsum 从0开始元素的累积和
# cumprod 从1开始元素的累积积
# percentile  0-100 百分位数
# quantile    分位数  median 中位数

# 7.12 一维数组
a = np.array([1,2,3,4,3,5,3,6])
print(f'数组：{a}')
print(np.sum(a))
print(np.prod(a))
print(np.cumsum(a))          # 从0开始元素的累积和
print(np.cumprod(a))         # 从1开始元素的累积积
print(np.max(a))
print(np.min(a))
print(np.argmax(a))          # 最大值所在的下标
print(np.argmin(a))          # 最小值所在的下标
print(np.mean(a))            # 平均数
print(np.median(a))          # 中位数
print(np.average(a))         # 加权平均

counts = np.bincount(a)      # 统计非负整数的个数，不能统计浮点数
print(np.argmax(counts))     # 返回众数,此方法不能用于二维数组

# Numpy中没有直接的方法求众数，但是可以这样实现：
# bincount（）：统计非负整数的个数，不能统计浮点数
counts = np.bincount(nums)
#返回众数
np.argmax(counts)

help(np.bincount)
#Count number of occurrences of each value in array of non-negative ints.

# 二维数组
from scipy import stats
a = np.array([[1,3,6],[9,2,3],[2,3,3]])
print(f'数组：\n{a}')
print('-'*30)
print(np.sum(a))
print(np.prod(a))
print(np.cumsum(a))    # 从0开始元素的累积和，返回一维数组
print(np.cumprod(a))   # 从1开始元素的累积积，返回一维数组
print(np.max(a))
print(np.min(a))
print(np.argmax(a))    # 按照一维排列
print(np.argmin(a))    
print(np.mean(a))      
print(np.median(a))    
print(np.average(a))  

# 数组的众数不建议在Numpy里面计算，在Pandas里面计算更简单。
# 将一维数组转成Pandas的Series,然后调用mode()方法
import pandas as pd
nums = np.random.randint(1,10,size=20)
ser = pd.Series(nums)
print(ser.mode())
# 将二维数组转成Pandas的DataFrame,然后调用mode()方法
nums1 = np.random.randint(1,10,size=20).reshape(4,5)
df = pd.DataFrame(nums1)
print(df)
print(df.mode())
































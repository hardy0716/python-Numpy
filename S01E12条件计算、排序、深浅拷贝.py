# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 12:00:34 2022

@author: 15517
"""

# 7.2.1  将条件逻辑作为数组操作
import numpy as np
a = np.array([[1,3,6],[9,3,2],[1,4,3]])
print(f'数组\n{a}')
print(a>3)
print(np.where(a>3,520,1314))  # where(条件,若满足返回值，不满足返回值)


# 7.2.2 布尔值数组方法 any 和 all
print((a>3).sum())   ## 数组中大于3的数有多少个
# 因为a > 3 返回的是布尔值True (1) 和 False (0) 

# 对于布尔值数组，有两个常用方法any和all。
# any：检查数组中是否  至少  有一个True
# all：检查是否每个值  都是  True

b = np.array([False,False,True,False])
print(b.any())   #返回True
print(b.all())   #返回False

# 7.2.3 按值大小排序 sort

# ndarray.sort(axis=-1, kind='quicksort', order=None)
# axis 排序沿数组的（轴）方向。0表示按行，1表示按列，None表示展开排序，默认为-1，表示沿最后的轴排序
# kind 排序的算法，提供了快排'quicksort'、混排'mergesort'、堆排'heapsort'; 默认为快排
# order 排序的字段名，可指定字段排序，默认为None

# 一维数组
a = np.array([3,6,7,9,2,1,8,5,4])
a.sort()    # sort会打乱原始数据的顺序
print(a)

# 二维数组
a = np.array([[0,12,48],[4,18,14],[7,1,99]])
print(a)
print(np.sort(a))            # 默认按最后的轴排序， （行，列） (0,1)
print(np.sort(a,axis=0))     # 按行排序

# 拓展：按字段名排序
dt = np.dtype([('name','S10'),('age',int)])
a = np.array([("Mike",21),("Nancy",25),('Bob',17),('Jane',27)],dtype = dt)
np.sort(a,order = 'name')
np.sort(a,order = 'age')



# 7.2.4 从大到小的索引 argsort
# numpy.argsort(a, axis=-1, kind='quicksort', order=None)
# 对数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。 这个索引数组用于构造排序后的数组。
# 参数类似于sort()
# 一维数组
x = np.array([59,29,39])

a = np.argsort(x)   # argsort 不会改变原始数据
print(a)
print(f'索引升序：{a}') # [1,2,0] 第一个最大，第二个最小，第三个中间  29 39 59
print(f'数组升序：{x[a]}')  # 以排序后的顺序重构原数组

b = np.argsort(-x)  # 降序
print(f'索引降序：{b}')
print(f'数组升序：{x[b]}')

# 二维数组
x = np.array([[0,12,48],[4,18,14],[7,1,99]])
print(x)
a1 = np.argsort(x)
print(f'索引排序：\n{a1}')

# 以排序后的顺序重构原数组，注意与一维数组的形式不一样
print(np.array([np.take(x[i],x[i].argsort()) for i in range(3)]))
# 如i=0时， x[i],x[i].argsort()  为[0,12,48],[0,1,2]  排序为[0,12,48]
# 如i=1时,  x[i],x[i].argsort()  为[4,18,14],[0,2,1]  排序为[4,14,18]


# ??????????????????????
# 7.2.5 根据键值的字典序进行排序 lexsort
# lexsort(keys, axis=-1)
# lexsort()根据键值的字典序进行排序，支持对数组按指定行或列的顺序排序，间接排序，不修改原数组，返回索引。一般对一维数组使用argsort()。
# 默认按最后一行元素有小到大排序, 返回最后一行元素排序后索引所在位置。
# keys 排序的参照物包括数组或N维的元组，默认值为最后一行，（二维则为最后一列）



# lexsort()  就是先按照最后一个轴排序（axis=-1）,如若存在相同值再按照倒数第二个，以此类推
# 比如最后一个轴的数据为[4,14,18] 则直接返回array([0,1,2])
# 若为[4,18,18] ,倒数第二个轴为[6,10,8] 则返回array([0,2,1])



x = np.array([[0,12,48],[4,18,14],[7,1,99]])
np.lexsort(x)   # 返回索引值 [1,0,2]
y = np.array([[6,10,8],[4,18,18]])
np.lexsort(y)   # [0,2,1] 
help(np.lexsort)

a = np.array([1,5,1,4,3,4,4])
b = np.array([9,4,0,4,0,2,1])
ind = np.lexsort((b,a))
ind # 将长度相同的a,b组合，再根据a值得大小进行排序，再考虑b值
# array([2, 0, 4, 6, 5, 3, 1], dtype=int64) 

list(zip(a[ind],b[ind]))

c = [[1,5,1,4,3,4,4],[9,4,0,4,0,2,1]]
np.lexsort(c)  #此种情况与先b后a的情况一致


# 其他方法
# 按最后一列顺序排序
x[np.lexsort(x.T)]

# 按最后一列逆序排序
x[np.lexsort(-x.T )]

# 按第一列顺序排序
x[np.lexsort(x[:,::-1].T)]

# 按最后一行顺序排序
x.T[np.lexsort(x)].T

# 按第一行顺序排序
x.T[np.lexsort(x[::-1,:])].T


# 7.2.6 唯一值与其他集合逻辑 unique 和 in1d
# 去重复
姓名 = np.array(['孙悟空','猪八戒','孙悟空','沙和尚','孙悟空','唐僧'])
print(np.unique(姓名))
数组 = np.array([1,3,1,3,5,3,1,3,7,3,5,6])
print(np.unique(数组))

#检查一个数组中的值是否在另外一个数组中，并返回一个布尔数组：
a = np.array([6,0,0,3,2,5,6])
print(np.in1d(a,[2,3,6]))


# unique(x)         #计算x的唯一值，并排序
# intersect1d(x,y)  #计算x和y的交集，并排序
# union1d(x,y)      #计算x和y的并集，并排序
# in1d(x,y)         #计算x中的元素是否包含在y中，返回一个布尔值数组
# setdiff1d(x,y)    #差集，在x中但不在y中的x元素
# setxor1d(x,y)     #异或集，在x或y中，但不属于x、y交集的元素



# 八、浅拷贝与深拷贝
# 浅拷贝
#a=b  不能这样赋值，因为a和b相互影响，在内存里a变了b也会发生变化 

# a=b[:] 视图操作，一种切片，会创建新的对象a，但是a的数据完全由b保管，他们两个的数据变化是一致的

# 深拷贝
# a=b.copy() 复制，a和b互不影响，相当于是重新开辟了一个空间保存b的值，然后让a指向b.copy()




















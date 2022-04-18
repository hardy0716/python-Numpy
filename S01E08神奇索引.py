# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 11:13:12 2022

@author: 15517
"""

import numpy as np
a = np.array([3,6,7,9,5,2,7])
print(a)
a[[2,3,5]]                       #返回对应下标的一组数 array([7, 9, 2])  

b = np.arange(36).reshape(9,4)
print(b)
print(b[[4,3,0,6]])              #返回第4行、第3行、第0行、第6行


c = np.arange(32).reshape(8,4)
print(c)
read = b[[1,5,7,2],[0,3,1,2]]    #读取第1行第0列、第5行第3列、第7行第1列、第2行第2列的数据
print(read)


d = np.arange(36).reshape(9,4)
print(d[:,[1,2]])                #打印d中      第1列、第二列的所有行的值


e = np.arange(10)
f = np.array([[0,2],[1,3]])
print(e[f])                     #?????????
# 提取的结果是：  第0行为e的第0和第2位置的数值，第1行为e的第1和第3位置的数字

e1 = np.arange(1,10,2)
print(e1[f])                    # 和上面的对比一下  



#实例 获取数组中最大的前N个数字
x = np.random.randint(1,100,10)   #1-100的10个随机数
print(x)

# 数组.argsort()会返回排序后的下标
y = x.argsort()
print(y) #返回数组中的下标

# 取最大值对应的3个下标，因为默认升序，所以要用-3,从倒数第3个到最后一个
y1 = x.argsort()[-3:]
print(y1)
#将下标传递给数组
xmax = x[y1]
print(f'最大的三个数为{xmax}')


















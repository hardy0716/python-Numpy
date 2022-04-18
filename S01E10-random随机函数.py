# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:38:00 2022

@author: 15517
"""
# 4.1seed向随机数生成器传递随即状态种子
import random
random.seed(10)
print(random.random())# random.random()用来随机生成一个0到1之间的浮点数，包括零。
print(random.random())
print(random.random())# 这里没有设置种子，随机数就不一样了


# 4.2 rand 返回[0,1]之间，均匀分布
import numpy as np
a = np.random.rand(3)  #一维
print(a)
b = np.random.rand(2,3) #二维
print(b)
c = np.random.rand(2,3,4) #三维
print(c)


import numpy as np
import matplotlib.pyplot as plt
# 绘制正弦曲线
x轴 = np.linspace(-10,10,100) # 在[-10,10]闭区间或半闭区间中，数量为100
y轴 = np.sin(x轴)  # sin正弦、cos余弦
plt.plot(x轴,y轴)
plt.show()


#加入噪声后
import numpy as np
import matplotlib.pyplot as plt
# 绘制正弦曲线
x = np.linspace(-10,10,100) # 在[-10,10]闭区间中，数量为100
y = np.sin(x) + np.random.rand(len(x))  # 生成均匀分布，len(x轴)就是维度，相加就是定义元素的相加
plt.plot(x,y)
plt.show()



# 4.3randn 返回标准正态分布随机数（浮点数）平均数0，方差1
a = np.random.randn(3)  #一维
print(a)
b = np.random.randn(2,3) #二维
print(b)
c = np.random.randn(2,3,4) #三维
print(c)

# 4.4randint 随机整数
a = np.random.randint(3)  
print(f'随机0至3之间的整数是：{a}')

b = np.random.randint(1,10)  
print(f'随机1至10之间的整数是：{b}')   

c = np.random.randint(1,10,size=(5,))
print(f'随机1至10之间取5个元素组成一维数组{c}')

d = np.random.randint(1,20,size=(3,4))
print(f'随机1至20之间取12个元素组成3行4列二维数组：\n{d}')

e = np.random.randint(1,20,size=(2,3,4))
print(f'随机1至20之间取24个元素组成两块3行四列三维数组：\n{e}')


# 4.5 random 生成0.0至1.0的随机数 浮点数
一维 = np.random.random(3)
print(f'生成3个0.0至1.0的随机数:\n{一维}')

二维 = np.random.random(size=(2,3))
print(f'生成2行3列共6个数的0.0至1.0的随机数:\n{二维}')

三维 = np.random.random(size=(3,2,3))
print(f'生成三块2行3列，每块6个数的0.0至1.0的随机数:\n{三维}')

# 4.6 choice 从一维数组中生成随机数

# 第一参数是一个1维数组，如果只有一个数字那就看成range(5)
# 第二参数是维度和元素个数，一个数字是1维，数字是几就是几个元素
a = np.random.choice(5,3)
print(f'从range(5)中拿随机数，生成只有3个元素的一维数组是：{a}')

b = np.random.choice(5,(2,3))
print(f'从range(5)中拿随机数，生成2行3列的数组是：\n{b}')


c = np.random.choice([1,2,9,4,8,6,7,5],3)
print(f'从[1,2,9,4,8,6,7,5]数组中拿随机数，3个元素：{c}')

d = np.random.choice([1,2,9,4,8,6,7,5],(2,3))
print(f'从[1,2,9,4,8,6,7,5]数组中拿随机数，生成2行3列的数组是：\n{d}')


# 4.7 shuffle(数组)把一个数进行随机排列
a = np.arange(10)
print(f'没有随机排列前的一维数组{a}')
np.random.shuffle(a)
print(f'随机排列后的一维数组{a}')   # a本身的顺序被随机排列打乱


b = np.arange(20).reshape(4,5)
print(f'没有随机排列前的二维数组{b}')
np.random.shuffle(b)
print(f'随机排列后的二维数组{b}')

# 二维数组随机排列只按行随机，列是不变的


c = np.arange(12).reshape(2,2,3)
print(f'没有随机排列的三维数组\n{c}\n')
np.random.shuffle(c)
print(f'随机排列后的三维数组\n{c}\n')

# 三维数组随机排列只按块随机，行和列是不变的


#4.8 permutation(数组) 把一个数组随机排列或者数字全排列
# 与4.7shuffle一样都是将数据重新排列
#  不同点在于 permutation不会改变原有数据的顺序，而是新建一个变量

a = np.random.permutation(10)    # 10 ~ range(10) 
print(a)

b = np.arange(9).reshape(3,3)
print(f'没有随机排列前的二维随机数组\n{b}\n')
b1 = np.random.permutation(b)
print(f'随机排列后的二维数组是\n{b1}\n')
print(f'查看初始的二维数据是否发生变化\n{b}\n')


# 4.9 normal 生成正态分布数字
#   normal [平均值mean，标准差sd，size]
x = np.random.normal(1,10,10)  #均值为1，标准差为10，10个数
print(x)


# 4.10 uniform 均匀分布
# uniform(low,high,size)
y = np.random.uniform(1,10,10)   #最小值为1，最大值为10，10个数
print(f'在1~10之间生成10个随机数:\n{y}\n')

y1 = np.random.uniform(1,10,(2,3))
print(f'在1~10之间生成2行3列的随机数：\n{y1}\n')



















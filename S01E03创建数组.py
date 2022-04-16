import numpy as np
# a = np.array([1,2,3,4,5])
# b = np.array(range(1,6))
# c = np.arange(1,6)   #推荐使用
# print(a.dtype)  #int32
# print(type(a))  #<class 'numpy.ndarray'>

# 给数据指定数据类型
# d = np.array(range(1,8),dtype=float) #修改数据类型
# e = np.array(range(1,8),dtype='float32') #修改数据类型和位数
#
# print(d)
# print(e)
# print(d.dtype) #float64
# print(e.dtype) #float32
# print(type(d)) #<class 'numpy.ndarray'>
# print(type(e)) #<class 'numpy.ndarray'>


#array：将输入的数据（可以是列表、元组、数组以及其它序列）转换为ndarray(Numpy数组)，
#如不显示指明数据类型，将自动推断，默认复制所有输入数据。

#arange：Python内建函数range的数组版，返回一个数组。

# array的属性：
# • shape：返回一个元组，表示 array的维度 [形状，几行几列] （2，3）两行三列，（2，2，3）两个两行三列
# print(a.shape)  #(5,)  5行1列
# # • ndim：返回一个数字，表示array的维度的数目
# print(a.ndim)   # 1维
# # • size：返回一个数字，表示array中所有数据元素的数目
# print(a.size)  # 5个元素
# # dtype：返回array中元素的数据类型
# print(a.dtype)  #int32


#使用arange创建数字序列：
# np.arange([开始,]结束[,步长],dtype=None)  #推荐
# a = np.arange(5)  # 返回[0 1 2 3 4]
# print(a)
# b = np.arange(1,10,2)  #返回[1 3 5 7 9]
# print(b)

#1.1.2 使用ones 创建全是1的数组
# np.ones(shape,dtype=None,order='C')
# shape：整数或者整型元组定义返回数组的形状；可以是一个数（创建一维向量），也可以是一个元组（创建多维向量）
# dtype : 数据类型，可选定义返回数组的类型。
# order : {‘C’, ‘F’}, 可选规定返回数组元素在内存的存储顺序：C（C语言）-rowmajor；F（Fortran）column-major

# a = np.ones(3)  #返回[1. 1. 1.]
# print(a)
#
# b = np.ones((2,3))  #两行三列的 数组
# print(b)
#
# c = np.ones((5,),dtype=None) #[1. 1. 1. 1. 1.]
# print(c)

#1.1.3 ones_like 创建形状相同的数组
#np.ones_like(a,dtype=float,order='C',subok=True)
#返回：与a相同形状和数据类型的数组，并且数组中的值都为1
# subok ： bool，可选。True：使用a的内部数据类型，False：使用a数组的数据类型，默认为True

# 案例1
# x = np.array([[0,1,2],
#           [3,4,5]])
# print(np.ones_like(x))  #返回 2行3列的 1
#
# #案例2
# y = np.array([0.,1.,2.])
# print(np.ones_like(y))


#1.1.4 zeros 创建全是0的数组
# np.zeros(shape,dtype=None,order='C')
# a = np.zeros(10) #返回：[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# print(a)
#
# b = np.zeros((2,4))  # 2行4列
# print(b)

#1.1.5 zeros_like  创建形状相同的数组
# np.zeros(a,dtype=None)
# # 案例1
# x = np.array([[0,1,2],
#              [3,4,5]])
# print(np.zeros_like(x))
# # 案例2
# y = np.array([0.,1.,2.])  # 返回：[0. 0. 0.]
# print(np.zeros_like(y))



#1.1.6 full创建指定值的数组
#np.full(shape,fill_value,dtype=None,order='C')
#fill_value：标量（就是纯数值变量）
# x = np.full(3,520) 
# print(x)
# print(np.full((2,4),520))
# print()


# 1.1.7 full_like 创建开关相同的指定值数组
# np.full_like(a,fill_value,dype=None)
# 案例1
# x1 = np.array([[0,1,2],
#                [3,4,5]])
# print(x1)
# print(np.full_like(x1,520))
# print()

# 案例2
# y1 = np.array([0.,1.,2.])
# print(y1)
# print(np.full_like(y1,520))



#1.1.8 使用random模块生成随机数组
import random
# np.random.randn(d0,d1,...dn)

a = np.random.randn()   #一个随机数
b = np.random.randn(3)   #3个数
c = np.random.randn(3,2)  #3行2列
d = np.random.randn(3,2,4)  #3块，每块是2行4列
print(d)



























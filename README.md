# python-Numpy
Numpy 基础学习



# 数组
  array：将输入数据（可以是列表、元组、数组以及其它序列）转换为ndarray(Numpy数组)，如不显示指明数据类型，将自动推断，默认复制所有输入数据。
  arange：Python内建函数range的数组版，返回一个数组。
  
 # array的属性：
  shape：返回一个元组，表示 array的维度 [形状，几行几列] （2，3）两行三列，（2，2，3）两个两行三列
  ndim：返回一个数字，表示array的维度的数目
  size：返回一个数字，表示array中所有数据元素的数目
  dtype：返回array中元素的数据类型!

# 使用arange创建数字序列：
# np.arange([开始,]结束[,步长],dtype=None)

# 使用ones创建数字序列
# np.ones(shape,dtype=None,order='C')
# order : {‘C’, ‘F’}, 可选规定返回数组元素在内存的存储顺序：C（C语言）-rowmajor；F（Fortran）column-major。
# ones_like
# np.ones_like(a,dtype = float, order = 'C',subok = True)  # 输出为与a形状相同的数组，填充全为1
# 参数
order顺序 ： {'C'，'F'，'A'或'K'}，可选,覆盖结果的内存布局。
subok ： bool，可选。True：使用a的内部数据类型，False：使用a数组的数据类型，默认为True!


# 使用zeros创建数字序列                  # 同ones

# full  创建指定值的数组
# np.full(shape,full_value, dtype=None , order = 'C')
# full_like 同zeros、ones

# 使用random生成随机数
# np.random(d0,d1,d2..)
# a = np.random.randn()         # 一个随机数
# b = np.random.randn(3)       #  3个数
# c = np.random.randn(3,2)     # 3行2列
# d = np.random.randn(3,2,4)  # 3块，每块是2行4列

# np.round(a,2)  # 变量a 保留2位小数

# reshape  不改变值，修改形状
# a = np.arange(10).reshape(2,5)   #变为2行5列
# b = a.reshape(10) = a.reshape(1,10)      # 变回1行10列
# c = a.flatten()        #直接转为1堆


# 广播规则
如果两个数组的后缘维度（trailing dimension，即从末尾开始算起的维度）的轴长度相符，或其中的一方的长度为1，则认为它们是广播兼容的。广播会在缺失和（或）长度为1的维度上进行。
# 这句话乃是理解广播的核心。广播主要发生在两种情况，一种是两个数组的维数不相等，但是它们的后缘维度的轴长相符，另外一种是有一方的长度为1。
# （3，2，3） 和 （2，3）   后缘(2,3) 可以运算
# （3，2，3） 和 （3，）    后者为1维，可以运算
# （3，2，2） 和 （2，1）   后者最后为1 可以扩充为(2,2)
# （3，2，3） 和 （2，4）   后者为(2,4) != (2,3)  不能运算


# 基础索引与切片
a = np.arange(10)
A = np.arange(20).reshape(4,5)
# 一维数组---语法： 序列[开始位置下标:结束位置下标:步长]
print(a[3],a[5],a[-1])  # 3 5 9
# 二维数组  #索引行列坐标，类似EXCEl
print(A[0,0])           # 0行0列位置  0
print(A[-1,2])          # 最后一行第二列  17  
print(A[2])             # 第二行  [10 11 12 13 14]
print(A[-1])            #最后一行 [15 16 17 18 19]
print(A[0:-2])          #除了最后两行
print(A[0:2,2:4])       #第0、1两行的第2、3两列的四个数
print(A[:,2])           #第2列所有数
# 切片修改  （会改变原来的数组）
a[4:6] = 520    #第4、5位置的数值修改为520  # [0,1,2,3,520,520,6,7,8,9]
A[:1,:2] = 520  #第0行的第0、1列修改为520

# 布尔值  Ture False
一维数组
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
print(b[fil2])          # 返回所有为True的对应数字组成的数组，以一维数组展现 [11,12,13,14,15,16,17,18,19,20]

# 条件组合：找出偶数或小于7的数
c = np.arange(10)
print(c)
condition = (c%2 ==0) | (c < 7)
print(condition)
print(c[condition])

# 神奇索引
a = np.array([3,6,7,9,5,2,7])
print(a)
a[[2,3,5]]                       #返回对应下标的一组数 array([7, 9, 2]) 

b = np.arange(36).reshape(9,4)
print(b)
print(b[[4,3,0,6]])              #返回第4行、第3行、第0行、第6行


e = np.arange(10)   #[0,1,2,3,4,5,6,7,8,9]
print(e)
f = np.array([[0,2],[1,3]])
print(e[f])                     #[[0,2],[1,3]]
e1 = np.arange(1,10,2)
print(e[f])                     #[[1,5],[3,7]]
提取的结果是：  第0行为e的第0和第2位置的数值，第1行为e的第1和第3位置的数字


# 实例 获取数组中最大的前N个数字

x = np.random.randint(1,100,10)   #1-100的10个随机数
print(x)
y = x.argsort() # 数组.argsort()会返回排序后的下标
print(y) #返回数组中的下标
y1 = x.argsort()[-3:] # 取最大值对应的3个下标，因为默认升序，所以要用-3,从倒数第3个到最后一个
print(y1)
xmax = x[y1]   #将下标传递给数组
print(f'最大的三个数为{xmax}')

# 元组的轴和转置
# 数组转置换轴
data = np.arange(15).reshape(3,5)
print(data.shape)   # (3,5)
print(data.T)
print(data.T.shape)  #(5,3)

print(data.reshape(5,3))   # 输出结果会有差异  reshape 会以按照行的位置抽取数值，也就是将数组按行排列为一维，然后逐个按照reshape（）排列

# transpose()   行列转置   transpose = T
x = np.arange(24).reshape(4,6)
print(x)
print(x.transpose())    

# swapaxes 轴转置
print(x.swapaxes(1,0))   # x.shape=(4,6),对应元组索引为[0,1] 经swapaxes(1,0) 就是将0轴和1轴互换位置

# 轴转置心得
# 三维数组在进行轴转置时， 不变的维的数据 不动
arr = np.arange(16).reshape(2,2,4)  # 2块，2行4列的数组
print(arr)

arr.transpose((1,0,2))          #块和行转置，shape为（2，2，4） ，
列的顺序不变，行和块之间进行变换

arr.transpose((2,1,0))          #块和列转置，shape为（4,2,2）
行的顺序不变，列和块之间进行变换  

arr.transpose(0,2,1)            #行和列转置，shape为(2,4,2)


# swapaxes和transpose 没什么区别
transpose( *, *,*)  有三个参数 初始为(0,1,2) 
swapaxes(*, *) 有两个参数

arr.transpose(1,0,2)  # 0 和 1 互换
arr.swapaxes(1,0)    # 0 和 1 互换
即 arr.transpose(1,0,2) = arr.swapaxes(1,0) 

# random 随机函数
 import random
 
 
# seed() 向随机数生成器传递随机状态种子
random.seed(10)  
print(random.random())  # 每次都输入种子之后，打印的随机数都是相同的

rand 返回[0,1]之间的服从均匀分布的数据
a = np.random.rand(3)  #一维  
b = np.random.rand(2,3) #二维 
c = np.random.rand(2,3,4) #三维 


randn 返回服从标准正态分布的随机数(浮点数) X ~ N(0,1)
a = np.random.randn(3)  #一维 
b = np.random.randn(2,3) #二维  
c = np.random.randn(2,3,4) #三维  

randint 随机整数
a = np.random.randint(3)  # 0~2之间的随机整数 
b = np.random.randint(1,10)   # 1~9之间的随机整数
c = np.random.randint(1,10,size=(5,))  #1~9之间随机5个整数  取得值会重复 因为每一个值都是独立抽取的
d = np.random.randint(1,20,size=(3,4))  # 1~19之间 随机3行4列   共12个随机整数
e = np.random.randint(1,20,size=(2,3,4))  # 1~19之间 随机2块3行4列 


random 生成0.0至1.0的随机数 浮点数
一维 = np.random.random(3)
二维 = np.random.random(size=(2,3))
三维 = np.random.random(size=(3,2,3))


choice 从一维数组中生成随机数
   第一参数是一个1维数组，如果只有一个数字那就看成range(5)
   第二参数是维度和元素个数，一个数字是1维，数字是几就是几个元素，一次类推
a = np.random.choice(5,3)
b = np.random.choice(5,(2,3))
c = np.random.choice([1,2,9,4,8,6,7,5],3)
d = np.random.choice([1,2,9,4,8,6,7,5],(2,3))


shuffle(数组)把一个数进行随机排列
a = np.arange(10)
print(a)
np.random.shuffle(a)
print(a)   #shuffle 会将原始数组顺序改变

# 二维数组随机排列只按行随机，列是不变的
b = np.arange(20).reshape(4,5)
print(b)
np.random.shuffle(b)
print(b)

# 三维数组随机排列只按块随机，行和列是不变的
c = np.arange(12).reshape(2,2,3)
print(c)
np.random.shuffle(c)
print(c)

permutation(数组) 把一个数组随机排列或者数字全排列
与shuffle一样都是将数据重新排列,不同点在于 permutation不会改变原有数据的顺序，而是新建一个变量

a = np.random.permutation(10)    # 10 ~ range(10) 
print(a)


normal 生成正态分布数字     normal [平均值mean，标准差sd，size]
x = np.random.normal(1,10,10)  #均值为1，标准差为10，10个数
print(x)

uniform 均匀分布
uniform(low,high,size)
y = np.random.uniform(1,10,10)   #最小值为1，最大值为10，10个数

# 通用函数ufunc
  是一种在ndarray数组中进行逐元素操作的函数

# 一元ufunc 函数
sqrt(a)  a的平方根；  exp(a)  a的自然指数幂

# 二元ufunc 函数
add, maximum, minimum 
x = np.random.randn(8)    # randn从标准正态分布中得到的随机变量
y = np.random.randn(8)
print(np.maximum(x,y))   # 对位比较大小，取大的，生成新的数组返回，逐个元素地将 x和 y 中元素的最大值计算出来

# 还要好多函数 自己总结！！！！！！！！！！！！！
sign(x)  # 计算各元素的正负号~   1：正； -1:负； 0：零
ceil 天花板 floor 地板 rint 四舍五入取整数
print(np.modf(x))        # modf 将数组中数据的小数位和整数位两部分独立写开
print(np.mod(5,4))       # mod(除数，被除数)  返回余
...........
...........
...........
...........
...........


# 数学和统计方法
prod 乘积；  argmin,argmax 最小和最大值的位置
cumsum 从0开始元素的累积和
cumprod 从1开始元素的累积积
percentile  0-100 百分位数
quantile    分位数  median 中位数

# Numpy中没有直接的方法求众数，但是可以这样实现：
            bincount（）：统计非负整数的个数，不能统计浮点数
nums = np.array([0,0,2,4,8,7,1,5,5,47,52,5,0,0])
counts = np.bincount(nums)
#返回众数
np.argmax(counts)
            argmax()  返回沿轴的最大值的索引

数组的众数不建议在Numpy里面计算，在Pandas里面计算更简单。
# 将一维数组转成Pandas的Series,然后调用mode()方法
import pandas as pd
nums = np.random.randint(1,10,size=20)
ser = pd.Series(nums)
print(ser.mode())


# Numpy的axis参数的用途
axis = 0 代表行，  axis = 1 代表列
所有的数学和统计函数都有这个参数，

a = np.array([[1,3,6],[9,3,2],[1,4,3]])
print(f'数组\n{a}')
print(np.sum(a,axis = 0))  # 按行相加 即 1+9+1；3+3+4；6+2+3
print(np.sum(a,axis = 1))  # 按列相加 即 1+3+6； 9+3+2； 1+4+3
# axis = 0 求每列的和    axis = 1 求每行的和  # 思考Excel的运算



# 条件计算、排序、深浅拷贝

将条件逻辑作为数组操作
a = np.array([[1,3,6],[9,3,2],[1,4,3]])
print(a>3)  #返回布尔值
print(np.where(a>3,520,1314))  # where(条件,若满足返回值，不满足返回值)


布尔值数组方法 any 和 all
print((a>3).sum())   ## 数组中大于3的数有多少个，a>3 返回几个True
因为a > 3 返回的是布尔值True (1) 和 False (0) 


对于布尔值数组，有两个常用方法any和all。
# any：检查数组中是否  至少  有一个True
# all：检查是否每个值  都是  True

b = np.array([False,False,True,False])
print(b.any())   #返回True
print(b.all())   #返回False

# 按值大小排序 sort

# ndarray.sort(axis=-1, kind='quicksort', order=None)
axis 排序沿数组的（轴）方向。0表示按行，1表示按列，None表示展开排序，默认为-1，表示沿最后的轴排序
kind 排序的算法，提供了快排'quicksort'、混排'mergesort'、堆排'heapsort'; 默认为快排
order 排序的字段名，可指定字段排序，默认为None

从大到小的索引 argsort
# numpy.argsort(a, axis=-1, kind='quicksort', order=None)
# 对数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。 这个索引数组用于构造排序后的数组。

一维
x = np.array([59,29,39])
a = np.argsort(x)   # argsort 不会改变原始数据
print(a)  # 返回[1,2,0]
print(f'数组升序：{x[a]}')  # 以排序后的顺序重构原数组 [29,39,59]
# b = np.argsort(-x)  # 降序

二维
x = np.array([[0,12,48],[4,18,14],[7,1,99]])
print(x)
a1 = np.argsort(x)
print(f'索引排序：\n{a1}')   #返回的是 各行的顺序索引

# 以排序后的顺序重构原数组，注意与一维数组的形式不一样
print(np.array([np.take(x[i],x[i].argsort()) for i in range(3)]))
如i=0时， x[i],x[i].argsort()  为[0,12,48],[0,1,2]  排序为[0,12,48]
如i=1时,  x[i],x[i].argsort()  为[4,18,14],[0,2,1]  排序为[4,14,18]



# 7.2.5 根据键值的字典序进行排序 lexsort
# lexsort(keys, axis=-1)
# lexsort()根据键值的字典序进行排序，支持对数组按指定行或列的顺序排序，间接排序，不修改原数组，返回索引。一般对一维数组使用argsort()。
# 默认按最后一行元素由小到大排序, 返回最后一行元素排序后索引所在位置。
# keys 排序的参照物包括数组或N维的元组，默认值为最后一行，（二维则为最后一列）


# lexsort()  就是先按照最后一个轴排序（axis=-1）,如若存在相同值再按照倒数第二个，以此类推
# 比如最后一个轴的数据为[4,14,18] 则直接返回array([0,1,2])
# 若为[4,18,18] ,倒数第二个轴为[6,10,8] 则返回array([0,2,1])


按最后一列顺序排序
x[np.lexsort(x.T)]

按最后一列逆序排序
x[np.lexsort(-x.T )]

按第一列顺序排序
x[np.lexsort(x[:,::-1].T)]

按最后一行顺序排序
x.T[np.lexsort(x)].T

按第一行顺序排序
x.T[np.lexsort(x[::-1,:])].T



# 唯一值与其他集合逻辑 unique 和 in1d      去重复
姓名 = np.array(['孙悟空','猪八戒','孙悟空','沙和尚','孙悟空','唐僧'])
print(np.unique(姓名))
数组 = np.array([1,3,1,3,5,3,1,3,7,3,5,6])
print(np.unique(数组))

#检查一个数组中的值是否在另外一个数组中，并返回一个布尔数组：
a = np.array([6,0,0,3,2,5,6])
print(np.in1d(a,[2,3,6]))


# unique(x)         #计算x的唯一值，并排序
# intersect1d(x,y)  #计算x和y的 交集 ，并排序
# union1d(x,y)      #计算x和y的 并集 ，并排序
# in1d(x,y)         #计算  x  中的元素是否  包含 在  y  中，返回一个布尔值数组
# setdiff1d(x,y)    #差集，在x中但不在y中的x元素
# setxor1d(x,y)     #异或集，在x或y中，但不属于x、y交集的元素


# 深拷贝与浅拷贝
浅拷贝
a=b  不能这样赋值，因为a和b相互影响，在内存里a变了b也会发生变化
a=b[:] 视图操作，一种切片，会创建新的对象a，但是a的数据完全由b保管，他们两个的数据变化是一致的

# 深拷贝
a=b.copy() 复制，a和b互不影响，相当于是重新开辟了一个空间保存b的值，然后让a指向b.copy()










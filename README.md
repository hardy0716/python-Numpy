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














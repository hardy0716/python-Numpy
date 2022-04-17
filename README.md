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
# （3，2，3） 和 （2，4）   后者为(2,4) != (2,3)  不可以运算


























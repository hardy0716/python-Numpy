#题目： 数组a与数组b相加，数组a是1~N数字的立方，数组b是1~N数字的平方
#   py计算
def 加法(n):
    a = [i**3 for i in range(1,n+1)]
    b = [i**2 for i in range(1,n+1)]
    c = []
    for i in range(n):
        c.append(a[i]+b[i])
    return c
print(加法(3))



# numpy 计算
import numpy as np
def 数组相加(n):
    a = np.arange(1,n+1) ** 3
    b = np.arange(1,n+1) ** 2
    return a+b
print(数组相加(3))

#由于Python是先循环遍历再计算，Numpy直接计算，计算数量越大越节省时间。





import numpy

ins_array = numpy.array([[1, 2, 3], [4, 5, 6]])

print(ins_array)
print("维数:\t", ins_array.ndim)
print("行列数:\t", ins_array.shape)
print("大小:\t", ins_array.size)


a = numpy.array([1, 2, 3], dtype=numpy.float)
print("a矩阵的数据类型：" + str(a.dtype))

# 定义一个3行4列的零矩阵
b = numpy.zeros((3, 4))      # 默认是float64
print("b矩阵的数据类型：" + str(b.dtype))


c = numpy.zeros((2, 5), dtype=numpy.int)
print(c)

# 定义一个单位矩阵
d = numpy.ones((3, 3))      # 默认是float64
print(d)

# 定义一个空矩阵
e = numpy.empty((3, 4))
print(e)


f = numpy.arange(0, 10, 2)  # 从0到10每隔2生成一个数据
# 左闭右开区间
print(f)

# 生成12个数，并重新排列为3行4列
g = numpy.arange(12).reshape((3, 4))
print(g)

h = numpy.linspace(1, 10, 20).reshape(4,5)      # 从1到10分为20段
print(h)
import numpy
import math

A = numpy.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = numpy.array([
    [7, 8, 9],
    [1, 2, 3],
    [4, 5, 6]
])

E = numpy.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])


E_c1 = numpy.array([
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]
])

E_r1 = numpy.array([
    [1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]
])

#【矩阵运算】
print("A + B = ")
print(A + B)


print("与？？矩阵相乘\n", E * A)
print("=====" * 10)
print(E, "\n", A)
print("=====" * 10)

print(E_c1 * A)

print(E_r1 * A)


print(A ** 2)
print(A ** 3)

#【三角函数】
angle = numpy.array([0, 30, 45, 60, 90, 180])
print(math.pi/180)
sin_value = numpy.sin(angle * ((2*(math.pi))/360))
cos_value = numpy.cos(angle * ((2*(math.pi))/360))
print(sin_value)
print(cos_value)

#【判断大小】
print(A < 3)
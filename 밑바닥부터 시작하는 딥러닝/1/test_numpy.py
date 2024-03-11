import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([4.0, 5.0, 6.0])

sum = x + y
# print(sum)

broadcast = x / 2.0
# print(broadcast)

A = np.array([[1,2], [3,4]])
B = np.array([[3,0], [0,6]])

# 형상
print(A.shape)
# 자료형
print(A.dtype)

sum2 = A + B
# print(sum2)



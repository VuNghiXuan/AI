import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model

# Data
x = [2,9,7,9,11,16,25,23,22,29,29,35,37,40,46]
y = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

x = np.array([x]).T
y = np.array([y]).T

# Vẽ đồ thị
title = plt.figure("Hướng dẫn 4. Bài 2 code công thức gradient") # tên đồ thị
contruct_axes = plt.axes(xlim=(-10, 60), ylim=(-1, 20))
plt.plot(x, y, 'ro')

# gán lr cho thuật toán sklearn
lr = linear_model.LinearRegression()

# huấn luyện cho thuật toán lr
lr.fit(x,y)

# Muốn vẽ thuật toán thì phải xác định nhiều điểm li ti trên trục x
# 


# print ("x:", x)
# print ("y:", y)

plt.show()
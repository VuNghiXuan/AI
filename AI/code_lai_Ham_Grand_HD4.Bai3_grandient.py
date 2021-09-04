from matplotlib import colors
import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
from numpy.core.numeric import ones
from scipy.sparse import linalg
from sklearn import linear_model
import sklearn
import random

""" hàm tính f(x) hay cost(x): x là hệ số a,b: 
Vetor Ax nghĩa là mặt phẳng chứa hình chiếu của vector y
Trog đó x là vector a, b | x = [[a], [b]
vector a, b nghĩa là kéo dài vector theo x để tìm hình chiếu vector p trên mặt phẳng:
 """ 
# hàm tính f(x) hay cost(x):
def cost(x): # hay vecot chứa a, b
    "f(x) = (1/2m) * |Ax-y|^2; với (1/2m) để khi áp dụng f'(x) triệt tiêu đi 2"
    m = A.shape[0]
    return (0.5/m)* np.linalb.norm((A.dot(x)-y)**2, 2)

# Tính đạo hàm tìm vetor ab_new
def grand(x):
    "f(x) = |Ax-y|^2, Gọi m là số phần tử trong list x "
    "f(x) = (1/2m) * |Ax-y|^2; với (1/2m) để khi áp dụng f'(x) triệt tiêu đi 2"
    "f'(x) = (1/2m)*2*A*(Ax-y)--> công thứ đạo hàm (u)^n'= n.u'.(u)^(n-1)"
    "=> f'(x) = (1/m) * A*(Ax-y)"
    m = A.shape[0]
    # chú ý A*: phải chuyển chiều mới * dc 2 ma trận, vector phải dùng .dot
    return (1/m) * A.T.dot(A.dot(x)-y)
    
    # ValueError: shapes (15,2) and (15,1) not aligned: 2 (dim 1) != 15 (dim 0)


# Tìm vector a_b
def grand_descent(a_b, alpha, count):
    "Vị trí x0-> x0-alpha*f'(x)"
    a_b_new = [a_b]

    for i_count in range(count):
        ab = a_b_new[-1] - alpha*grand(a_b_new[-1])
        a_b_new.append(ab)
    return a_b_new

# Data
x = [2,9,7,9,11,16,25,23,22,29,29,35,37,40,46] # 1 list có 1 hàng
y = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

" 1. Vẽ đường thẳng theo x, y"
x= np.array([x]).T
y= np.array([y]).T

matric_ones = np.ones_like(x)
A = np.concatenate((x, matric_ones), axis=1)
ax = plt.axes(xlim = (-10,60), ylim = (-2,20))
plt.plot(x, y,'ro')

" 2. Huấn luyện điển (x,y) Vẽ đường thẳng đi qua giữa theo thuật toán sklearn"
# gán thuật toán 
lr  = linear_model.LinearRegression()
lr.fit(A, y)

x_min = np.min(x)
x_max = np.max(x)
x_min_max = np.linspace(x_min, x_max, 2)

y_sklearn = lr.coef_[0][0] * x_min_max + lr.intercept_[0]
plt.plot(x_min_max, y_sklearn, color = "green")

" 3. Vẽ đường thằng bất kỳ"
# create vector a_b bất kỳ
a_b = np.array([[1],[2]]) #a_b: là vector có độ dốc a, chặn tung tại b

# y=ax+b
y_rand = a_b[0][0]*x_min_max + a_b[1][0]

plt.plot(x_min_max, y_rand, color = "gray")

" 4. Tịnh tiến y_rand ---> y_sklearn: Cho x-->x0"
# Ta có: cost(x)--> f(x) = |Ax-y|^2 
# Grendient f'(x): cho x->x0, tính độ dốc giảm dần đến cực trị
"Tức là f'(x) - alpha * count  "
alpha = 0.0001 #mỗi lần tiến tới cực trị là 0.0001
count = 100 # với count = Số lần tịnh tiến 
a_b_count = grand_descent(a_b, alpha, count) # vector a_b_count: ứng với số lần tịnh tiến 

for i_ab in a_b_count:
    y_count = i_ab[0][0]*x_min_max + i_ab[1][0]
    plt.plot(x_min_max, y_count, color = "gray")

plt.show()

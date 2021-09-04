from matplotlib import colors
import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
from numpy.core.numeric import ones
from scipy.sparse import linalg
from sklearn import linear_model
import sklearn
import random
import matplotlib.animation as amimation

""" hàm tính f(x) hay cost(x): x là hệ số a,b: 
Vetor Ax nghĩa là mặt phẳng chứa hình chiếu của vector y
Trog đó x là vector a, b | x = [[a], [b]
vector a, b nghĩa là kéo dài vector theo x để tìm hình chiếu vector p trên mặt phẳng:
 """ 
# hàm tính f(x) hay cost(x):
def cost(ab): # hay vecot chứa a, b
    "f(x) = (1/2m) * |Ax-y|^2; với (1/2m) để khi áp dụng f'(x) triệt tiêu đi 2"
    m = A.shape[0]
    return 0.5/m * np.linalg.norm(A.dot(ab) - y, 2)**2    

# Kiểm tra công thức đạo hàm:
"f'(x0) = f(x0 + eps) - f(x0 - eps)/2*eps"
def check_grad(ab):
    eps = 1e-4
    f_gradx = np.zeros_like(ab)
    for i_x0 in range(len(ab)):
        x1 = ab.copy()
        x2 = ab.copy()
        x1[i_x0] += eps
        x2[i_x0] -= eps

        check_grads = (cost(x1) - cost(x2))/(2*eps)
        f_gradx[i_x0] = check_grads
    
    # tính đạo hàm bằng hàm grad(x)
    calcular_grap = grad(ab)
    # check gần đúng:
    if np.linalg.norm(calcular_grap - f_gradx) > 1e-7:
        print("CHECK HÀM GRAD_X!!!")

# Tính đạo hàm tìm vetor ab_new
def grad(ab):
    "f(x) = |Ax-y|^2, Gọi m là số phần tử trong list x "
    "f(x) = (1/2m) * |Ax-y|^2; với (1/2m) để khi áp dụng f'(x) triệt tiêu đi 2"
    "f'(x) = (1/2m)*2*A*(Ax-y)--> công thứ đạo hàm (u)^n'= n.u'.(u)^(n-1)"
    "=> f'(x) = (1/m) * A*(Ax-y)"
    m = A.shape[0]
    # chú ý A*: phải chuyển chiều mới * dc 2 ma trận, vector phải dùng .dot
    return (1/m) * A.T.dot(A.dot(ab)-y)
    # 1/m * A.T.dot(A.dot(x)-b)

# Tìm vector a_b
def grand_descent(a_b, alpha, count):
    "Vị trí x0-> x0-alpha*f'(x)"
    a_b_new = [a_b]
    
    for i_count in range(count):
        ab = a_b_new[-1] - alpha*grad(a_b_new[-1])

        " 5. Tìm vị trí điểm dừng của x-->x0, khi gần với cực trị"
        # Dừng thuật toán vì tiến đến gần cực trị
        # np.linalg: thư viện tuyến tính, tính CDài vector
        # norm(grand(a_b_new[-1])): tính khoảng cách 2 vector a,b
        # ab ->0 thức là cực trị
        
        if np.linalg.norm(grad(ab))/len(ab) <0.5: #/len(ab)            
            break           
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
fig1 = plt.figure("gradient")
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
a_b = np.array([[2.], [1.]]) #a_b: là vector có độ dốc a, chặn tung tại b

# y=ax+b
y_sklearn = a_b[0][0]*x_min_max + a_b[1][0]

plt.plot(x_min_max, y_sklearn, color = "gray")

" 4. Tịnh tiến y_sklearn ---> y_sklearn: Cho x-->x0"
# Ta có: cost(x)--> f(x) = |Ax-y|^2 
# Grendient f'(x): cho x->x0, tính độ dốc giảm dần đến cực trị
"Tức là f'(x) - alpha * count  "
alpha = 0.0001 #mỗi lần tiến tới cực trị là 0.0001
interate = 80 # với count = Số lần tịnh tiến 
a_b_count = grand_descent(a_b, alpha, interate) # vector a_b_count: ứng với số lần tịnh tiến 

# Kiểm tra tính đạo hàm:    
check_grad(a_b)

for i, i_ab in enumerate(a_b_count):
    y_count = i_ab[0][0]*x_min_max + i_ab[1][0]
    plt.plot(x_min_max, y_count, color = "gray", alpha = 0.5)


# Vẽ amimation
line, =ax.plot([], [], color = "red")
# print(line); chứa trả về 2 cái list ([], [], color = "black")

def update(i): #i: tạm hiểu amimation là index của từng vector ab
    y_sk = a_b_count[i][0][0]*x_min_max + a_b_count[i][1][0]
    line.set_data(x_min_max, y_sk)
    return line,

iters = np.arange(1, len(a_b_count), 1) # số 1 cách nhau 1 đơn vị
run = amimation.FuncAnimation(fig1, update, iters, interval=50, blit = True) # tốc độ 50

# Thêm chú thích: legend
plt.legend(('Value in each GD interation', "Sulution by formular", 'Inital value for GD'), loc=(0.52,0.01))
# loc=(0.52,0.01) : đặt góc phải bên dưới
l_text = plt.gca().get_legend().get_texts

# Tên biểu đồ
plt.title("Gradient Descent")

# print (len(a_b_count))

"-------------------Đoạn này ko sử dụng kể từ bài 6, vĩ thay cho amimation"
# " 6. Vẽ đồ thị cost(x)"
# x_interates = []
# y_ab_counts = []

# for i_ab, y_ab in enumerate(a_b_count):
#     x_interates.append(i_ab)
#     y_ab_counts.append(cost(y_ab))

# plt.plot(x_interates, y_ab_counts)
# plt.xlabel('x_interates')
# plt.ylabel('y_ab_counts')
"-------------------Sử dụng amimation"
plt.show()

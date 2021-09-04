from matplotlib import colors
import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
from scipy.sparse import linalg
from sklearn import linear_model
import sklearn
import random

# tính f(x) = (1/2m).|Ax-y|^2
def cost(A): # A là ma trận có chứa ma vector 1 đơn vị
    m = A.shape[0]
    # f(x) = 0.5/m|Ax-y|^2    
    return (0.5/m) * np.linalb.norm(A.dot(x)-y, 2)**2
    # linalb.norm: hàm tính khoảng cách:
    # Số 2 khoảng cách (x1-x2), số 2 dưới dấu bình phương |Ax-y|^2 # với"2 dưới |"

def grand(x): # f'(x) = 1/m*AT*(Ax-y)
    m = A.shape[0]
    return (1/m) * A.T.dot(A.dot(x)-y)

def grandient_desent(a_b, learn_rate, iteration): # iteration: n_lan số lần muốn đi xuống 
    # Hàm này trả về 2 danh sách mỗi lần tịnh tiến
    a_b_list = [a_b]
    for n in range(iteration):
        a_b_new = a_b_list[-1] - (learn_rate * grand(a_b_list[-1]))
        a_b_list.append(a_b_new)
    return a_b_list 
   

# Data
x = [2,9,7,9,11,16,25,23,22,29,29,35,37,40,46] # 1 list có 1 hàng
y = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# Xử lý bằng array  
x = np.array([x]).T # mỗi hàng là 1 list thì mới vẽ dc
ones = np.ones_like(x, dtype = np.uint8)

# Ma trận Ax: là Ma trận gồm vector x với vector 1 đơn vị
A = np.concatenate((x, ones), axis=1)

y = np.array([y]).T


# tên đố thị
plt.figure("LinearRegression")

# Giới hạn số trên trục
ax = plt.axes(xlim = (-10, 60), ylim = (-1,20))
plt.plot(x, y,'ro')

"scikit-learn / sk-learn, gói học máy trong Python, để thực hiện hồi quy tuyến tính cho một tập hợp các điểm dữ liệu."
"y = mx + b , trong đó m  là độ dốc và b là giao thoa."
"Cắt trục (y) tại điểm có tung độ bằng b, b được gọi là tung độ gốc của đường thẳng"
"Mục tiêu là tìm ra các giá trị tốt nhất của độ dốc ( m ) và chặn ( b ) để phù hợp với dữ liệu của chúng tôi."
"Hồi quy tuyến tính sử dụng phương pháp bình phương tối thiểu thông thường để phù hợp với các điểm dữ liệu "

# Giải bài toán chung
"Hoặc: y = ax1 + bx2 + cx3 + d"
"Trong đó: l.intercept-->[d]"#intercept : đánh chặn (d) cho phù hợp
"          l.coef---> [[a],[b],[c]]"#, coef: đá ngầm, là các hệ số độ dốc 

# Khai báo hàm hồi quy tuyến tính và gọi  fit phương thức để tìm hiểu từ dữ liệu:
lr = linear_model.LinearRegression()# linear_model: mô hình tuuyến tính, LinearRegression: dg thẳng hồi quy

# Huấn luyện hàm hồi quy theo dữ liệu (x,y)
lr.fit(x,y)

x_min = np.min(x)
x_max = np.max(x)
point_x = 2
# print(x_min, x_max)

# Gán x_min_to_max: phân bố theo trục x với các điểm li ti
x_min_to_max = np.linspace(x_min, x_max, point_x) # linspace: lấy đều từ min--> max = số điểm points=2

# Dự đoán y_sklearn theo pt dg thang y = ax+b, với a,b là 1 vector [[a][b]]
# print(lr.coef_)>>>[[0.32798834]] và print(lr.intercept_)>>>[1.56559767]
y_sklearn = lr.coef_[0][0]*x_min_to_max + lr.intercept_[0] 

plt.plot(x_min_to_max, y_sklearn, color="green")#, color = "green")
# print(x_min_to_max, y_sklearn)

# Vẽ đườg thẳng y=ax+b bất kỳ, chọn ngẫn nhiên hệ số a,b 
a=random.randint(1,2)
b=random.randint(1,2)
a_b = np.array([[a],[b]])

y_init = a_b[0]*x_min_to_max + a_b[1]
plt.plot(x_min_to_max, y_init, color = "black")

# thuật toán gradient: đạo hàm để thay đổi đường thẳng đi xuống theo công thức
"tức x0 = x0 - alpha*f'(x) mỗi lần xuống 1 tí đến cực trị nếu là parabol"  

learn_rate = 0.0001
n = 100
a_b_list = grandient_desent(a_b, learn_rate, n) #a_b là điểm ban đầu và mỗi lần đạo trừ đi 1 tí (còn gọi độ dốc)
# learn_rate, tức là alpha
# print(a_b)


for a_b in a_b_list:
    y_list = a_b[0]*x_min_to_max + a_b[1]
    plt.plot(x_min_to_max, y_list, color = "gray")

plt.show()

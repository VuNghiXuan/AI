import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import shape

# x = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# y = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]

x = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
y = [40,35,10,9,11,16,19,18,22,15,22,35,37,40,37,35,39,31,30,28,35,2,10,6]

plt.plot(x, y, "ro") # "ro": biễu diễn điểm

" I. Tìm và vẽ phương trình đường thẳng gần dự đoán, đi qua giữa đồ thị  " 
" I.1 Tìm hệ số a, b từ phương trình y= ax+b"
"=====> Áp dụng công thức [[a],[b] = {(A^T * A) ^-1} *A^T * y  tham khảo hình 4" 

"       I.1.1 Viết công thức ma trận A:"
# a/ Đổi list x, y về ma trận theo dạng cột
# print(np.array(x[:, 1]**2).T)


x = np.array([x]).T # np.array nhận tham số là 1 list trong list để hiểu là cột
y = np.array([y]).T

x_quadratic = np.array(x[:]**3) #quadratic equation : PT bậc 3
x_squar = np.array(x[:]**2)
# print("x_quadratic", x_quadratic)

# b/ Tạo ma trận đơn vị với các phhần từ = 1, kích thước = x và nối vào x để thành A
shape_x = x.shape[0]
shape_y = x.shape[1]
ones = np.ones((shape_x, shape_y), dtype= np.uint8)
A = np.concatenate((x_quadratic, x_squar, x, ones), axis = 1)
A_T = A.T # matrix transpose : Ma trận chuuyển vị A

# Tìm inverse matrix: Ma trận nghịch đảo của công thức: (A^T * A) ^-1
matrix_inv = np.linalg.inv(A_T.dot(A)) # inverse matrix: Ma trận nghịch đảo

# Tìm hệ số a, b = matrix_inv * A^T * y theo ptrình y = ax+b
a_b_c_d = matrix_inv.dot(A_T).dot(y) # kết quả >>>[[a][b]] = [[0.32361847] [1.88039364]]

"Vẽ phương trình dg thẳng dự đoán (đi qua giữa cá điểm) khi đã biết a,b "
" Ta có y = ax + b"
"Chọn x0: gồm 2 điểm thuộc đồ thị đã dc vẽ trên đồ thị" 
"  ===> ở đây chọn 2 điểm gần tọa độ và cuối đồ thị x_min =2, x_max = 46"
x_min = np.min(x)
x_max = np.max(x)

# x0 = np.array([[x_min, x_max]]).T # x0: là 1 list nhận nhiều điểm, 
x0 = np.linspace(x_min,x_max,10000) # x0: hàm np.linspace nah65n vào int, 10000 vị trí bc nhảy bên trong 

# y0= a.x0^3 + b.x0 ^2 + c.x0 + d 
y0 = a_b_c_d[0][0]*x0*x0*x0 + a_b_c_d[1][0]*x0*x0 + a_b_c_d[2][0]*x0 + a_b_c_d[3][0]

# Vẽ đường thẳng y0= a.x0 + b
plt.plot(x0, y0)

# Test dự đoán điểm x_question = 12. 
"Tìm y_question = ???"

x_question = 12
y_question = a_b_c_d[0][0]*x_question*x_question*x_question + a_b_c_d[1][0]*x_question*x_question + a_b_c_d[2][0]*x_question + a_b_c_d[3][0]
print(y_question)

# Vẽ đồ thị
plt.show()
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
def cost(ab, A, y): # hay vecot chứa a, b
    "f(x) = (1/2m) * |Ax-y|^2; với (1/2m) để khi áp dụng f'(x) triệt tiêu đi 2"
    m = A.shape[0]
    return 0.5/m * np.linalg.norm(A.dot(ab) - y, 2)**2    

# Kiểm tra công thức đạo hàm:
"f'(x0) = f(x0 + eps) - f(x0 - eps)/2*eps"
def check_grad(ab, A, y):
    eps = 1e-4
    f_gradx = np.zeros_like(ab)
    for i_x0 in range(len(ab)):
        x1 = ab.copy()
        x2 = ab.copy()
        x1[i_x0] += eps
        x2[i_x0] -= eps

        check_grads = (cost(x1, A, y) - cost(x2, A, y))/(2*eps)
        f_gradx[i_x0] = check_grads
    
    # tính đạo hàm bằng hàm grad(x)
    calcular_grap = grad(ab, A, y)
    # check gần đúng:
    if np.linalg.norm(calcular_grap - f_gradx) > 1e-7:
        print("CHECK HÀM GRAD_X!!!")

# Tính đạo hàm tìm vetor ab_new
def grad(ab, A, y):
    "f(x) = |Ax-y|^2, Gọi m là số phần tử trong list x "
    "f(x) = (1/2m) * |Ax-y|^2; với (1/2m) để khi áp dụng f'(x) triệt tiêu đi 2"
    "f'(x) = (1/2m)*2*A*(Ax-y)--> công thứ đạo hàm (u)^n'= n.u'.(u)^(n-1)"
    "=> f'(x) = (1/m) * A*(Ax-y)"
    m = A.shape[0]
    # chú ý A*: phải chuyển chiều mới * dc 2 ma trận, vector phải dùng .dot
    return (1/m) * A.T.dot(A.dot(ab)-y)
    # 1/m * A.T.dot(A.dot(x)-b)

# Tìm vector a_b
def grand_descent(a_b, A, y, alpha, count):
    "Vị trí x0-> x0-alpha*f'(x)"
    a_b_new = [a_b]
    
    for i_count in range(count):
        ab = a_b_new[-1] - alpha*grad(a_b_new[-1], A, y)

        " 5. Tìm vị trí điểm dừng của x-->x0, khi gần với cực trị"
        # Dừng thuật toán vì tiến đến gần cực trị
        # np.linalg: thư viện tuyến tính, tính CDài vector
        # norm(grand(a_b_new[-1])): tính khoảng cách 2 vector a,b
        # ab ->0 thức là cực trị
        
        if np.linalg.norm(grad(ab, A, y))/len(ab) <0.3: #/len(ab)            
            break           
        a_b_new.append(ab)
    return a_b_new


# Tạo vector x, y, one, x_squar  và ma trận A 
def create_vector_xy_matric_A(x, y):
    x_vec = np.array([x]).T
    y_vec = np.array([y]).T
    x_squar = np.array(x_vec)
    x_squar = x_squar[:]**2    
    ones_vec = np.ones_like(x_vec)
    matric_A = np.concatenate((x_squar, x_vec, ones_vec), axis=1)
    return x_vec, y_vec, matric_A

# Tìm abc vector hình chiếu p: 
def abc_formular(matric_A, y_vec):
    A_T = matric_A.T   
    # Tìm inverse matrix: Ma trận nghịch đảo của công thức: (A^T * A) ^-1
    matrix_inv = np.linalg.inv(A_T.dot(matric_A)) # inverse matrix: Ma trận nghịch đảo

    # Tìm hệ số a, b = matrix_inv * A^T * y theo ptrình y = ax+b
    abc = matrix_inv.dot(A_T).dot(y_vec) # kết quả >>>[[a][b]] = [[0.32361847] [1.88039364]]
    return abc

# Vẽ biểu đồ point thực tế 
def draw_point(x, y):
    fig1 = plt.figure("gradient_parabol")
    x_min = np.min(x) 
    x_max = np.max(x) + 10
    y_min = np.min(y) - 20
    y_max = np.max(y) + 10

    ax = plt.axes(xlim = (x_min, x_max), ylim = (y_min, y_max))
    return fig1, ax 

# tìm x_min, x_max trong list
def possive_x_parabol(x):
    x_min = np.min(x)
    x_max = np.max(x)
    x_linespace = np.linspace(x_min, x_max, 50).T
    return x_linespace

# Trả về tọa độ y theo x, và hệ số abc
def return_y_parabol(abc, x):
    return abc[0][0]*x*x + abc[1][0]*x + abc[2][0]

# trả về return_y_fit_parabol(abc, x)
def y_fit_linear(x0, A):    
    lr = linear_model.LinearRegression()
    lr.fit(x0, A)
    y0 = lr.coef_*x0**2 + lr.coef_*x0 + lr.intercept_
    return y0
    
# Tìm hệ số abc random từ fit 
def random_abc_10_percent(x, y, A):
    lr = linear_model.LinearRegression()
    lr.fit(A[::10], y[::10])
    abc_init = np.array([[lr.coef_[0][0]], [lr.coef_[0][1]], [lr.intercept_[0]]])
    # x_init = np.array([[-0.7], [7.], [-15.]])
    # x0_gd = np.linspace(-2, 35, 100)
    y0_gd = abc_init[0][0]*x**2 + abc_init[1][0]*x + abc_init[2][0]
    return abc_init, y0_gd
    
def main():
    # Data
    x = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    y = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]

    " 1. Vẽ thực tế điểm các points theo x, y "
    fig1, ax = draw_point(x, y)
    plt.plot(x, y, 'ro')
    # plt.show()

    " 2. Vẽ parabol theo x, y thực tế"
    " ------- Methol 1: ---- "
    x_minMax, y_vec, matric_A = create_vector_xy_matric_A(x, y)
    abc = abc_formular(matric_A, y_vec)
    
    # x_min_max = possive_x_parabol(x) #Biểu diễn x theo parabol
    y_prbol = return_y_parabol(abc, x_minMax)
    
    plt.plot(x_minMax, y_prbol, color = "green")
    # plt.show()

    " ------- Methol 2: sử dụng linear "
   
    # lr = linear_model.LinearRegression()
    # lr.fit(matric_A, y_vec)
    # # draw parabole
    # x0_lg = np.linspace(0, 30, 100)
    # y0_lg = lr.coef_[0,0]*x0_lg**2 + lr.coef_[0,1]*x0_lg + lr.intercept_
    # plt.plot(x0_lg, y0_lg, color="green")

    # plt.show()

    " 3. Vẽ parabol bất kỳ từ vector a_b bất kỳ"

    "Methol 1: random chọn 10%"
    # abc_init, y_rand = random_abc_10_percent(x_minMax, y_vec, matric_A)
    # plt.plot(x_minMax, y_rand, color = "black")
    
    "***** ----- ******print(abc) #để chọn abc_init cho gần đúng"
    abc_init = np.array([[-0.4], [6.], [-15.]])
    # x0_gd = np.linspace(-2, 35, 100)
    y0_gd = abc_init[0][0]*x_minMax**2 + abc_init[1][0]*x_minMax + abc_init[2][0]
    plt.plot(x_minMax, y0_gd, color = "black")
    # plt.show()    

    " 4. Tịnh tiến y_sklearn ---> y_sklearn: Cho x-->x0"
    # Ta có: cost(x)--> f(x) = |Ax-y|^2 
    # Grendient f'(x): cho x->x0, tính độ dốc giảm dần đến cực trị
    "Tức là f'(x) - alpha * count  "

    alpha = 0.000001 #mỗi lần tiến tới cực trị là 0.0001
    interate = 100 # với count = Số lần tịnh tiến 
    abc_count = grand_descent(abc_init, matric_A, y_vec, alpha, interate) # vector a_b_count: ứng với số lần tịnh tiến 

    # Kiểm tra tính đạo hàm:    
    check_grad(abc, matric_A, y_vec)

    for i, i_ab in enumerate(abc_count):
        y_count = i_ab[0][0]*x_minMax**2 + i_ab[1][0]*x_minMax + i_ab[2][0]
        plt.plot(x_minMax, y_count, color = "gray", alpha = 0.5)


    # Vẽ amimation
    line, =ax.plot([], [],  color = "red")
    # print(line); chứa trả về 2 cái list ([], [], color = "black")

    def update(i): #i: tạm hiểu amimation là index của từng vector ab
        y_sk = abc_count[i][0][0]*x_minMax**2 + abc_count[i][1][0]*x_minMax + abc_count[i][2][0] 
        line.set_data(x_minMax, y_sk)
        return line,

    iters = np.arange(1, len(abc_count), 1) # số 1 cách nhau 1 đơn vị
    run = amimation.FuncAnimation(fig1, update, iters, interval=50, blit = True) # tốc độ 50

    # Thêm chú thích: legend
    plt.legend(('Value in each GD interation', "Sulution by formular", 'Inital value for GD'), loc=(0.52,0.01))
    # loc=(0.52,0.01) : đặt góc phải bên dưới
    l_text = plt.gca().get_legend().get_texts

    # Tên biểu đồ
    plt.title("Gradient Descent")

    # print (len(a_b_count))
    plt.show()
    "-------------------Đoạn này ko sử dụng kể từ bài 6, vĩ thay cho amimation"
    " 6. Vẽ đồ thị cost(x)"
    x_interates = []
    y_ab_counts = []

    for i_ab, y_ab in enumerate(abc_count):
        x_interates.append(i_ab)
        y_ab_counts.append(cost(y_ab, matric_A, y))

    plt.plot(x_interates, y_ab_counts)
    plt.xlabel('x_interates')
    plt.ylabel('y_ab_counts')
    "-------------------Sử dụng amimation"
    
    plt.show()
if __name__ =="__main__":
    main()
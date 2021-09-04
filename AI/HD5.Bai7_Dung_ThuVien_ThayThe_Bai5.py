from sklearn import datasets, neighbors
import numpy as np

# Sử dụng thư viện đề tách huấn luyện chia 150 bộ với 100 là train, 50 là test
from sklearn.model_selection import train_test_split
# train_test_split: huấn luyện từ list test bằng chia cắt

from sklearn.metrics import accuracy_score as acc_score

# Tải thư viện các loài hoa iris
iris = datasets.load_iris()
iris_X = iris.data # [sepal lenght, sepal wieght, petal lenght, petal wieght]
iris_Y = iris.target # label màu chứa [0,1,2]
# print(iris.data) #dữ liệu thông số dài rộng từng loại cánh
# print(iris.target) # label: có 3 màu 0,1,2

"""
+ iris.data: gồm có:
+ sepal lenght: chiều dài loại cánh hoa dài nhất (sepal: đài hoa)
+ sepal wieght: chiều rộng đài hoa 
+ petal lenght: chiều dài loại cánh hoa (petal: đài hoa)
+ petal wieght: chiều rộng cánh hoa"""

# Xáo trộn index trong list loài hoa
    # a = np.array([1,2,3])
    # index = np.array([0,2,1])
    # a = a[index]
    # print (a)

randIndex = np.arange(len(iris_X))
np.random.shuffle(randIndex) #shuffle hàm random chọn ngẫu nhiên
iris_X = iris_X[randIndex]
iris_Y = iris_Y[randIndex]

# print(iris_X)
# print(iris_Y)

"Thay thế bằng thư viện sklearn"
# "cắt 100 hoa huấn luyện, 50 loài để test"
# X_train = iris_X[:100,:] # dấu (,:) là lấy hết cái list bên trong, do là 4 chiều
# X_test = iris_X[100:,:]
# Y_train = iris_Y[:100]
# Y_test = iris_Y[100:]
# print(X_train,X_test, Y_train, Y_test )

# train_test_split: huấn luyện từ list test bằng chia cắt
X_train,X_test, Y_train, Y_test = train_test_split(iris_X, iris_Y, test_size= 50)
"test_size= 50 : cho bộ test = 50 trong tổng 100"
# print(X_train,X_test, Y_train, Y_test )

# tìm và chọn 5 điểm gần nhất (giữa X_train, và X_test)
knn = neighbors.KNeighborsClassifier(n_neighbors= 5) # tương ứng k=5  bài 5

# Huấn luyện điểm và label 
knn.fit(X_train, Y_train)

# Dự đoán label
Y_predict = knn.predict(X_test)

# print(Y_predict)
# print(Y_test)

# Sử dụng from sklearn.metrics import accuracy_score as acc_score
acc = acc_score(Y_predict, Y_test)
print(acc)
# Sử dụng sklear.metric tính tỉ lệ trùng 
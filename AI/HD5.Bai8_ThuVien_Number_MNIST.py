from sklearn import datasets, neighbors
import numpy as np

# Sử dụng thư viện đề tách huấn luyện chia 150 bộ với 100 là train, 50 là test
from sklearn.model_selection import train_test_split
# train_test_split: huấn luyện từ list test bằng chia cắt

from sklearn.metrics import accuracy_score 

# Tải thư viện matplotlib xem ảnh
import matplotlib.pyplot as plt 

"1 Tải thư viện MNIST (số) "
digit = datasets.load_digits()
digit_X = digit.data # [sepal lenght, sepal wieght, petal lenght, petal wieght]
digit_Y = digit.target # label màu chứa [0,1,2]
# print(digit.data) #dữ liệu thông số dài rộng từng loại cánh
# print(digit.target) # label: có 3 màu 0,1,2

# print(digit_Y) # 
## len(digit_Y) >>> 1797 điểm dữ liệu, là label
## print(digit_Y) >>> [0 1 2 ... 8 9 8]: số 0,1,2...

# print(digit_X)
## digit_X.shape: [0]>>> 1797 vector; [1]>>> 64
## digit_X[0]: bức ảnh đầu tiên, hay vector của bức ảnh gồm 64 con số khác nhau, 
## mỗi con số là từ 0-> 255 (GRB); 64 = (chiều 8 x 8)

"""
+ digit.data: gồm có:
+ 1797 bức ảnh, mỗi bức ảnh có chiều (8x8), có màu trắng đen(màu RGB)từ 0->255
+ print(digit_Y) >>> [0 1 2 ... 8 9 8]: nhãn của các số 0,1,2...
+digit_X[0]: bức ảnh đầu tiên. Gồm các con số 0->255
"""

"Cách xem In bức ảnh đầu tiên" 
# img1 = digit_X[0]
# img1 = img1.reshape(8,8)
# plt.gray() # đổi qua trắng đen
# plt.imshow(img1)
# plt.show()
# print(digit_Y[0])

"Cách xem thống kê loại bức ảnh theo label: có bao nhiêu số 0, số 1, ...."
# plt.hist(digit_Y)
# plt.show()

" Xáo trộn các vetor bức ảnh trong tập hợp bức ảnh"
randIndex = np.arange(len(digit_X))
np.random.shuffle(randIndex) #shuffle hàm random chọn ngẫu nhiên
digit_X = digit_X[randIndex]
digit_Y = digit_Y[randIndex]

# print(digit_X)
# print(digit_Y)

"2. Tự viết thuật toán sklearn"
# "cắt 100 hoa huấn luyện, 50 loài để test"
# X_train = digit_X[:100,:] # dấu (,:) là lấy hết cái list bên trong, do là 4 chiều
# X_test = digit_X[100:,:]
# Y_train = digit_Y[:100]
# Y_test = digit_Y[100:]
# print(X_train,X_test, Y_train, Y_test )

"2. Sử dụng thuật toán sklearn từ train_test_split: huấn luyện từ list test bằng chia cắt" 

"Chia cắt 80 để train, 20% để test"
test_num = int(round(len(digit_X)*20/100,0)) 

X_train, X_test, Y_train, Y_test = train_test_split(digit_X, digit_Y, test_size= test_num)
"test_num= 359 : X_train còn lại = 1797-359 =1438 trong tổng 1797"
# print(X_train,X_test, Y_train, Y_test )

# tìm và chọn 5 điểm gần nhất (giữa X_train, và X_test)
knn = neighbors.KNeighborsClassifier(n_neighbors= 5) # tương ứng k=5  bài 5

# Huấn luyện điểm và label 
knn.fit(X_train, Y_train)

# Dự đoán label
Y_predict = knn.predict(X_test)

# print(Y_predict)
# print(Y_test)

# Sử dụng from sklearn.metrics tính tỷ lệ trùng
acc = accuracy_score(Y_predict, Y_test)
print(acc)

"* Cách test độ chính xác:"
" *.1 Hiển thị bức ảnh và test xem thuất toán dự đoán có đúng ko"
img_test = X_test[0]
img_test = img_test.reshape(8,-1) # chia thành 8 dòng, -1 ko cần xác định cột
# print(img_test)
plt.gray()
plt.imshow(img_test)
plt.show()

" *.2 Tìm label theo thư65t toán"
print(X_test[0].shape)
num_predict = knn.predict(X_test[0].reshape(1, -1)) #.reshape(1,-1)
# >>>[8]
print(X_test[0].shape)
print(num_predict)
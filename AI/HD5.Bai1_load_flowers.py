from sklearn import datasets
import numpy as np
import math
import operator

# hàm tính khoảng cách:
def get_distance(p1, p2):
    demensions = len(p1)    
    distance = 0
    for i_demen in range(demensions):
        distance += (p1[i_demen] - p2[i_demen])**2
    return math.sqrt(distance)

# get_k_neighborns : trả về danh sách k điểm gần nhất
def get_k_neighborns(training_X, label_y, point, k):
    # khoảng cách tất cả các point -> training_X
    # training_X : hiểu là 1 matrix
    distances = []

    # sau khi có k/c tìm khoảng cách ngắn nhất gán cho label
    neighborns = []
    for i_p in range(len(training_X)):
        distance = get_distance(training_X[i_p], point)
        distances.append((distance, label_y[i_p]))
    distances.sort(key = operator.itemgetter(0)) # itemgetter(0): vị trí đầu tiên của tupe
    for i_k in range(k):
        neighborn = distances[i_k][1]        
        neighborns.append(neighborn)    
    return neighborns

# highest_votes: trả về label màu nhiều nhất trong k = 5
def highest_votes(labels): # trả về label phổ biến nhất
    
    count_labels =[0,0,0] # vì chỉ có 3 label tương ứng [0,1,2]
    for label in labels:
        count_labels[label] +=1
    max_count = max(count_labels)
    index_label = count_labels.index(max_count)
    return index_label

# def hàm dự đoán
def predict(training_X, label_y, point, k):
    neighborns_labels = get_k_neighborns(training_X, label_y, point, k)
    # get_k_neighborns : trả về danh sách k điểm gần nhất
    # Ví dụ k= 5, là chọn 5 cái điểm gần nhất
    return highest_votes(neighborns_labels)
    # highest_votes: trả về label màu nhiều nhất trong k = 5

# Kiểm tra kết quả thu thập (%) độ chính xác so với bản gốc
def accuracy_score(predicts, labels): #Y_test chính là groudTruth: kết quả biết trước
    incorect_predicts = 0
    for i_label in range(len(labels)):
        if predicts[i_label] == labels[i_label]:
            incorect_predicts += 1
    acc = incorect_predicts/len(labels)
    return acc

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

"cắt 100 hoa huấn luyện, 50 loài để test"
X_train = iris_X[:100,:] # dấu (,:) là lấy hết cái list bên trong, do là 4 chiều
X_test = iris_X[100:,:]
Y_train = iris_Y[:100]
Y_test = iris_Y[100:]

k = 5
Y_predict = []
for point in X_test:
    label = predict(X_train, Y_train, point, k)
    Y_predict.append(label)

# print(Y_predict)
# print(Y_test)

# Kiểm tra kết quả thu thập (%) độ chính xác so với bản gốc
acc = accuracy_score(Y_predict, Y_test)
print(acc)


# print("Độ chính xác:", acc)
def dynamic_Programming(x):
    "Không truyền tham số y, nhưng vẫn hiểu đối số y"
    f = y
    return f

x = [2,9,7,9,11,16,25,23,22,29,29,35,37,40,46] # 1 list có 1 hàng
y = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

"Cách hoạt động: Dynamic Programming:"
"Truyền tham số ít nhất 1 tham số trong hàm main"
m = dynamic_Programming(x)
print("Kết quả Dynamic Programming:",  m)
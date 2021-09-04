import numpy as np

z = np.array([[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]])
print(z.shape)

# chia theo hàng
a = z.reshape(4,-1) #>>> (4,3)
b = z.reshape(-1,3) #>>> (4,3)
print(a.shape, b.shape)

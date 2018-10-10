import numpy as np
A = np.mat([
    [2, 1],
    [3, 4]], dtype=float)
a = np.linalg.det(A)
print(a)
B = np.mat([
    [3, 2, 1],
    [4, 9, 8],
    [5, 6, 7]], dtype=float)
b = np.linalg.det(B)
print(b)
# 3(63-48)-2(28-40)+(24-45)
# 3x15+2x12-21
# 45+24-21
# 48

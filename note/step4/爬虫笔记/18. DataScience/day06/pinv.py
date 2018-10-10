import numpy as np
A = np.mat([
    [11, 12, 13, 14],
    [20, 21, 22, 15],
    [19, 18, 17, 16]], dtype=float)
print(A)
B = np.linalg.pinv(A)
print(B)
print(A * B)

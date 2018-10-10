import numpy as np
A = np.mat([
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]], dtype=float)
print(A)
B = np.linalg.inv(A)
print(B)
C = A * B
print(C)
D = np.eye(3)
if (np.abs(C - D) < 1e-6).all():
    print('AA^-1 = ', D, sep='\n')

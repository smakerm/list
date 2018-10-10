import numpy as np
M = np.mat([
    [4, 11, 14],
    [8,  7, -2]], dtype=float)
print(M)
U, s, V = np.linalg.svd(M, full_matrices=False)
S = np.diag(s)
print(U, S, V, sep='\n')
print(U * S * V)
print(U * U.T)
print(V * V.T)

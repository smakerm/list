import numpy as np
A = np.mat([
    [3, -2],
    [1,  0]])
print(A)
eigvals = np.linalg.eigvals(A)
print(eigvals)
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)
for i, eigval in enumerate(eigvals):
    print(A * eigvecs[:, i])
    print(eigval * eigvecs[:, i])

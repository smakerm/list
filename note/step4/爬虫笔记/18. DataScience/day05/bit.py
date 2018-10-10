import numpy as np
a = np.array([1, -2, -3, 4, 5])
b = np.array([5, 4, -3, 2, -1])
c = a ^ b
print(a[np.where(c < 0)])
print(b[np.where(c < 0)])
d = np.arange(100)
print(d[np.where(d & (d - 1) == 0)])

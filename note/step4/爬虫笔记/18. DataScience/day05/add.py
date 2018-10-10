import numpy as np
a = np.arange(1, 7)
print(a)
b = np.add.reduce(a)
print(b)
c = np.add.accumulate(a)
print(c)
d = np.add.reduceat(a, [0, 2, 4])
# 0   2   4
# 1 2 3 4 5 6
# 3   7   11
print(d)
e = np.add.outer(a, d)
#   | 3  7 11
# --+--------
# 1 | 4  8 12
# 2 | 5  9 13
# 3 | 6 10 14
# 4 | 7 11 15
# 5 | 8 12 16
# 6 | 9 13 17
print(e)

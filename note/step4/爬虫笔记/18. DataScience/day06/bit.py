import numpy as np
a = np.array([1, -2, -3, 4, 5])
b = np.array([5, 4, -3, 2, -1])
c = a ^ b
print(a[np.where(c < 0)])
print(b[np.where(c < 0)])
d = np.arange(100)
print(d[np.where(d & (d - 1) == 0)])
e = np.arange(1, 21)
print(e)
f = e - 1
print(f)
# g = e & f
# g = e.__and__(f)
g = np.bitwise_and(e, f)
print(g)
h = e[g == 0]
print(h)
i = np.ones(5, dtype=int)
print(i)
j = i << 1
print(j)
k = j << 2
print(k)
l = np.arange(24)
print(l)
m = l % 4
print(m)
n = l & ((1 << 2) - 1)
print(n)

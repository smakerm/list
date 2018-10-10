import numpy as np
a = np.array([0, 2, 6, 3, 2, 7, 9, 4, 1, 9], dtype=float)
b = np.array([4, 2, 4, 7, 8, 6, 7, 2, 4, 4], dtype=float)
c = np.lexsort((b, a))
print(c)
print(a[c])
print(b[c])
d = np.lexsort((a, b))
print(d)
print(b[d])
print(a[d])
e = np.zeros(a.size).astype(np.complex64)
e.real = a
e.imag = b
print(e)
f = np.sort_complex(e)
print(f)
print(np.argmax(a), np.argmin(a))
a[1] = np.nan
print(a)
print(np.argmax(a), np.argmin(a))
print(np.max(a), np.min(a))
print(np.nanargmax(a), np.nanargmin(a))
print(np.nanmax(a), np.nanmin(a))
#             0  1  2  3  4  5
g = np.array([1, 2, 4, 6, 8, 9])
h = np.array([7, 3, 5])
i = np.searchsorted(g, h)
print(i)
j = np.insert(g, i, h)
print(j)
k = np.random.randint(10, 100, 20)
print(k)
#l = k[np.where(k % 2 == 0)]
#l = k[k % 2 == 0]
l = np.extract(k % 2 == 0, k)
print(l)
l[[1, 3, 5, 7]] = 0
print(l)
m = np.nonzero(l)
print(m)
print(l[m])

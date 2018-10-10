import numpy as np


def func(a, b):
    c = a + b
    d = a - b
    e = a * b
    return c, d, e

a = 1
b = 5
c, d, e = func(a, b)
print(c, d, e)

A = np.array([1, 2, 3, 4, 5])
B = np.array([5, 4, 3, 2, 1])

C, D, E = [], [], []
for a, b in zip(A, B):
    c, d, e = func(a, b)
    C.append(c)
    D.append(d)
    E.append(e)
C, D, E = np.array(C), np.array(D), np.array(E)
print(C, D, E, sep='\n')

C, D, E = np.hsplit(
    np.array([func(a, b) for a, b in zip(A, B)]).T.ravel(),
    3)
print(C, D, E, sep='\n')

C, D, E = np.frompyfunc(func, 2, 3)(A, B)
print(C, D, E, sep='\n')

C, D, E = A + B, A - B, A * B
print(C, D, E, sep='\n')


def funcs(b):
    def func(a):
        return a + b
    return np.frompyfunc(func, 1, 1)

print(funcs(B)(A))

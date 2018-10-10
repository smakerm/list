import numpy as np


def fun(a, b, c):
    return a + b + c

a, b, c = 10, 20, 30
d = fun(a, b, c)
print(d)

A = np.arange(1, 11)
B = np.arange(11, 21)
C = np.arange(21, 31)
D = np.vectorize(fun)(A, B, C)
print(D)

import numpy as np


def fibo1(n):
    if n <= 1:
        return 1
    return fibo1(n - 1) + fibo1(n - 2)


def fibo2(n):
    if n <= 1:
        return 1
    f0, f1 = 1, 1
    for i in range(2, n + 1):
        f2 = f1 + f0
        f0, f1 = f1, f2
    return f2


def fibo3(n):
    if n <= 1:
        return 1
    f = np.mat('1 1; 1 0')
    return (f ** n)[0, 0]


def fibo4(n):
    V = np.sqrt(5)
    return int((((1 + V) / 2)**(n + 1) -
                ((1 - V) / 2)**(n + 1)) / V)

n = 30
print(fibo1(n))
print(fibo2(n))
print(fibo3(n))
print(fibo4(n))

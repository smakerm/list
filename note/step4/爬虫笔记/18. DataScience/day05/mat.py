import numpy as np
a = np.matrix('1 2 6; 3 5 7; 4 8 9')
print(a)
b = np.mat(a)
print(b)
c = b.T
print(c)
d = c.I
print(d)
print(c * d)
e = np.mat([
    [1, 2, 6],
    [3, 5, 7],
    [4, 8, 9]], dtype=float)
print(e)
f = e.reshape(9)
print(f)
g = np.mat(np.array(
    [1, 2, 6, 3, 5, 7, 4, 8, 9])).reshape(3, 3)
print(g)
i = np.arange(1, 28).reshape(3, 3, 3)
print(i)
j = np.matrix(i[1])
print(j)
k = np.arange(1, 10).reshape(3, 3)
print(k)
#l = np.matrix(k)
#l = np.mat(k)
l = np.matrix(k, copy=False)
print(l)
l[1, 1] = 0
print(l)
print(k)
one = np.mat(np.ones(dtype=int, shape=(3, 3)))
print(one)
two = one * 2
print(two)
three = one + two
print(three)
four = three * 2 - two
print(four)
#
#    one | two
# -------+-------
#  three | four
#
#m = np.bmat('one two; three four')
# m = np.bmat([
#    [one,  two],
#    [three, four]])
m = np.bmat([one])
print(m)
m[1, 1] = 0
print(m)
print(one)
n = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
o = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]])
p = n * o
print(p)
q = np.mat(n)
r = np.mat(o)
s = q * r
print(s)

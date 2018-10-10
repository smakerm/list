import numpy as np
a = -np.add.outer(np.arange(1, 4) * 10, np.arange(1, 4))
print(a)
b = np.arange(1, 10).reshape(3, 3)
print(b)
c = np.divide(a, b)
#c = np.true_divide(a, b) # 同上
#c = a / b
#c = np.true_divide(a, b)
print(c)
#d = np.floor_divide(a, b)
d = a // b
print(d)
e = np.mod(a, b)
print(e)
f = np.fmod(a, b)
print(f)

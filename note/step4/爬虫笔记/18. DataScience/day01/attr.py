import os
import sys
import numpy as np


def main(argc, argv, envp):
    a = np.array([
        (1 + 1j, 2 + 4j, 3 + 7j),
        (4 + 2j, 5 + 5j, 6 + 8j),
        (7 + 3j, 8 + 6j, 9 + 9j)])
    print(a)
    print(type(a))
    print(type(a[0]))
    print(type(a[0][0]))
    print(a.dtype)
    print(a.dtype.type)
    print(a.dtype.str)
    print(a.dtype.char)
    print(a.dtype.itemsize)
    print(a.shape)
    print(a.ndim)
    print(len(a), a.size)
    print(a.itemsize)
    print(a.nbytes)
    print(a.T)
    print(a.real, a.imag, sep='\n')
    print(a.flat)
    for item in a.flat:
        print(item)
    print('-' * 6)
    print(a.flat[4])
    print('-' * 6)
    print(a.flat[[1, 3, 5]])
    a.flat[[2, 4, 6]] = 0
    print(a)
    b = a.tolist()
    print(b)
    #c = a.astype(np.str_)
    c = a.astype('U6')
    print(c)
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

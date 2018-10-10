import os
import sys
import numpy as np


def main(argc, argv, envp):
    a = np.arange(1, 7)
    print(a)
    b = a.reshape(2, 3)
    print(b)
    b[0][0] += 10
    print(b)
    print(a)
    c = b.reshape(6)
    print(c)
    d = b.ravel()
    print(d)
    e = b.flatten()
    print(e)
    e[0] += 10
    print(e)
    print(b)
    a.shape = (2, 3)
    print(a)
    print(c)
    a.resize((3, 2))
    print(a)
    f = a.transpose()
    print(f)
    #g = np.array([e]).transpose()
    g = e.reshape(-1, 1)
    print(g)
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

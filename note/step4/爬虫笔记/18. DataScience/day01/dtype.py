import os
import sys
import numpy as np


def main(argc, argv, envp):
    a = np.array([1, 2, 3], dtype='float32')
    print(a.dtype)
    b = np.array([
        (((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)),
         ((13, 14, 15, 16), (17, 18, 19, 20), (21, 22, 23, 24))),
        (((25, 26, 27, 28), (29, 30, 31, 32), (33, 34, 35, 36)),
         ((37, 38, 39, 40), (41, 42, 43, 44), (45, 46, 47, 48)))],
        #   dtype='>(2,3)4i4')
        dtype='>(2,3,4)i4')
    print(b)
    print(b.dtype)
    c = np.array([
        'Hello, World !',
        'Hello, Python !'],
        dtype=(np.str_, 14))
    print(c)
    print(c.dtype)
    d = np.array([
        (1, 2, 3, 4, 5),
        (6, 7, 8, 9, 10)], dtype=(int, 5))
    print(d)
    e = np.array([
        ((1, 2, 3), (4, 5, 6)),
        ((7, 8, 9), (10, 11, 12))],
        dtype=((np.uint8, 3), 2))
    print(e)
    f = np.array([('abc', 123), ('def', 456)],
                 dtype='U14, i4')
    print(f)
    print(f[0][0], f[0][1])
    g = np.array(
        [('abc', 123), ('def', 456)],
        dtype=[('name', np.str_, 14), ('age', np.int32)])
    print(g)
    print(g[0]['name'], g[0]['age'])
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

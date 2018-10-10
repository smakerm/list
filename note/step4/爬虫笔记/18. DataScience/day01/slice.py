import os
import sys
import numpy as np


def main(argc, argv, envp):
    a = np.arange(1, 10)
    print(a)
    print(a[:3])
    print(a[3:6])
    print(a[6:])
    print(a[::-1])
    print(a[:-4:-1])
    print(a[-4:-7:-1])
    print(a[-7::-1])
    print(a[::3])
    print(a[1::3])
    print(a[2::3])
    b = np.arange(1, 25).reshape(2, 3, 4)
    print(b)
    print(b[:, 0, 0])
    print(b[0, :, :])
    print(b[0, ...])
    print(b[0, 1, ::2])
    print(b[..., 1])
    print(b[:, 1])
    print(b[-1, 1:, 2:])
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

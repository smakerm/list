import os
import sys
import numpy as np


def main(argc, argv, envp):
    N = 5
    a = np.arange(1, 11)
    #b = np.ones(N) / N
    b = np.array([1, 2, 3, 4, 5]) / 15
    c = np.convolve(a, b[::-1], 'valid')
    print(a, b, c, sep='\n')
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

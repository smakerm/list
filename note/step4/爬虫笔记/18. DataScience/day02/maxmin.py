import os
import sys
import numpy as np


def main(argc, argv, envp):
    a = np.random.randint(10, 100, 27).reshape(
        3, 3, 3)
    print(a)
    print(np.max(a), np.min(a))
    print(np.maximum(np.maximum(a[0], a[1]), a[2]))
    print(np.minimum(np.minimum(a[0], a[1]), a[2]))
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

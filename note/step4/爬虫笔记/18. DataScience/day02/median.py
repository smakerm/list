import os
import sys
import numpy as np


def read_data(filename):
    closing_prices = np.loadtxt(
        filename, delimiter=',',
        usecols=(6), unpack=True,)
    return closing_prices


def auto_median(closing_prices):
    median = np.median(closing_prices)
    return median


def manu_median(closing_prices):
    scp = np.sort(closing_prices)
    median = (scp[int((scp.size - 1) / 2)] +
              scp[int(scp.size / 2)]) / 2
    return median


def main(argc, argv, envp):
    closing_prices = read_data('aapl.csv')
    print(auto_median(closing_prices))
    print(manu_median(closing_prices))
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

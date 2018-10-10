import os
import sys
import numpy as np


def read_data(filename):
    closing_prices = np.loadtxt(
        filename, delimiter=',',
        usecols=(6), unpack=True,)
    return closing_prices


def auto_mean(closing_prices):
    mean = np.mean(closing_prices)
    return mean


def manu_mean(closing_prices):
    tp = 0.
    for closing_price in closing_prices:
        tp += closing_price
    mean = tp / closing_prices.size
    return mean


def main(argc, argv, envp):
    closing_prices = read_data('aapl.csv')
    print(auto_mean(closing_prices))
    print(manu_mean(closing_prices))
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

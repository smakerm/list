import os
import sys
import numpy as np


def read_data(filename):
    highest_prices, lowest_prices = np.loadtxt(
        filename, delimiter=',',
        usecols=(4, 5), unpack=True,)
    return highest_prices, lowest_prices


def auto_vwap(closing_prices, volumes):
    vwap = np.average(closing_prices, weights=volumes)
    return vwap


def manu_vwap(closing_prices, volumes):
    vwp, tv = 0., 0.
    for closing_price, volume in zip(
            closing_prices, volumes):
        vwp += closing_price * volume
        tv += volume
    vwap = vwp / tv
    return vwap


def main(argc, argv, envp):
    highest_prices, lowest_prices = read_data(
        'aapl.csv')
    print(np.max(highest_prices))
    print(np.min(lowest_prices))
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

import os
import sys
import numpy as np


def read_data(filename):
    closing_prices, volumes = np.loadtxt(
        filename, delimiter=',',
        usecols=(6, 7), unpack=True,)
    return closing_prices, volumes


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
    closing_prices, volumes = read_data('aapl.csv')
    print(auto_vwap(closing_prices, volumes))
    print(manu_vwap(closing_prices, volumes))
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

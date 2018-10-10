import os
import sys
import datetime as dt
import numpy as np


def dmy2days(dmy):
    return (dt.datetime.strptime(
        str(dmy, encoding='utf-8'),
        '%d-%m-%Y').date() - dt.date.min).days


def read_data(filename):
    times, closing_prices = np.loadtxt(
        filename, delimiter=',',
        usecols=(1, 6), unpack=True,
        converters={1: dmy2days})
    return times, closing_prices


def auto_twap(times, closing_prices):
    twap = np.average(closing_prices, weights=times)
    return twap


def manu_twap(times, closing_prices):
    twp, tt = 0., 0.
    for time, closing_price in zip(
            times, closing_prices):
        twp += closing_price * time
        tt += time
    twap = twp / tt
    return twap


def main(argc, argv, envp):
    times, closing_prices = read_data('aapl.csv')
    print(auto_twap(times, closing_prices))
    print(manu_twap(times, closing_prices))
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

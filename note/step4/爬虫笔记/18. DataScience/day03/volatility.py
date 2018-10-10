import os
import sys
import numpy as np


def read_data(filename):
    closing_prices = np.loadtxt(
        filename, delimiter=',', usecols=(6), unpack=True)
    return closing_prices


def calc_volatility(closing_prices):
    log_closing_prices = np.log(closing_prices)
    log_rets = np.diff(log_closing_prices)
    log_rets_std = np.std(log_rets)
    volatility = log_rets_std / log_rets.mean() / \
        np.sqrt(1 / 252)
    return volatility


def main(argc, argv, envp):
    closing_prices = read_data('aapl.csv')
    volatility = calc_volatility(closing_prices)
    print(volatility)
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

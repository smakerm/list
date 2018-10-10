import os
import sys
import numpy as np


def read_data(filename):
    closing_prices = np.loadtxt(
        filename, delimiter=',',
        usecols=(6), unpack=True,)
    return closing_prices


def auto_returns(closing_prices):
    dif_prices = np.diff(closing_prices)
    returns = dif_prices / closing_prices[:-1]
    returns_std = np.std(returns)

    log_prices = np.log(closing_prices)
    log_returns = np.diff(log_prices)
    log_returns_std = np.std(log_returns)
    return returns_std, log_returns_std


def manu_returns(closing_prices):
    dif_prices = np.zeros(closing_prices.size - 1)
    for i, closing_price in enumerate(closing_prices):
        if i > 0:
            dif_prices[i - 1] = \
                closing_price - closing_prices[i - 1]
    sim_returns = np.zeros(dif_prices.size)
    for i, dif_price in enumerate(dif_prices):
        sim_returns[i] = dif_price / closing_prices[i]
    sim_returns_std = np.sqrt(
        ((sim_returns - sim_returns.mean())**2).mean())
    return sim_returns_std


def main(argc, argv, envp):
    closing_prices = read_data('aapl.csv')
    print('%f %f' % auto_returns(closing_prices))
    print(manu_returns(closing_prices))
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

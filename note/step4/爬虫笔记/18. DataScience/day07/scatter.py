import os
import sys
import platform
import numpy as np
import matplotlib.pyplot as mp


def read_data(filename):
    closing_prices, volumes = np.loadtxt(
        filename, delimiter=',', usecols=(6, 7),
        unpack=True)
    return closing_prices, volumes


def init_chart():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Price-Volume', fontsize=20)
    mp.xlabel('Price', fontsize=14)
    mp.ylabel('Volume', fontsize=14)

    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_chart(closing_prices, volumes,
               closing_price_rates, volume_rates):
    mp.scatter(closing_prices, volumes,
               s=closing_price_rates * 10000, c=volume_rates,
               cmap='prism', label='Price-Volume')
    mp.legend()


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    closing_prices, volumes = read_data('aapl.csv')
    closing_price_rates = np.diff(closing_prices) / \
        closing_prices[:-1]
    volume_rates = np.diff(volumes) / volumes[:-1]
    init_chart()
    draw_chart(closing_prices[:-1], volumes[:-1],
               closing_price_rates, volume_rates)
    show_chart()
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

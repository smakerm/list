import os
import sys
import platform
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    return dt.datetime.strptime(
        str(dmy, encoding='utf-8'),
        '%d-%m-%Y').date().strftime('%Y-%m-%d')


def read_data(filename):
    dates, opening_prices, highest_prices, \
        lowest_prices, closing_prices = np.loadtxt(
            filename, delimiter=',',
            usecols=(1, 3, 4, 5, 6), unpack=True,
            dtype=np.dtype('M8[D], f8, f8, f8, f8'),
            converters={1: dmy2ymd})
    return dates, opening_prices, highest_prices, \
        lowest_prices, closing_prices


def calc_profit(buying_rate, opening_price, highest_price,
                lowest_price, closing_price):
    buying_price = opening_price * buying_rate
    if lowest_price <= buying_price <= highest_price:
        profit = (closing_price - buying_price) * 100 / \
            buying_price
    else:
        profit = None
    return profit


def calc_profits(dates, buying_rates, opening_price, highest_price, lowest_price, closing_price):
    profits = np.vectorize(calc_profit)(
        buying_rates, opening_price, highest_price,
        lowest_price, closing_price)
    nan = np.isnan(profits)
    dates, profits = dates[~nan], profits[~nan]
    return dates, profits


def init_chart(buying_rate, first_day, last_day):
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Trading Simulation (%.2f%%)' % (
        buying_rate * 100), fontsize=20)
    mp.xlabel('Trading Days From %s To %s' % (
        first_day.astype(md.datetime.datetime).strftime(
            '%d %b %Y'),
        last_day.astype(md.datetime.datetime).strftime(
            '%d %b %Y')), fontsize=14)
    mp.ylabel('Profit Of BHP (%)', fontsize=14)
    ax = mp.gca()
    ax.xaxis.set_major_locator(
        md.WeekdayLocator(byweekday=md.MO))
    ax.xaxis.set_minor_locator(md.DayLocator())
    ax.xaxis.set_major_formatter(
        md.DateFormatter('%d %b %Y'))

    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_chart(dates, profits):
    dates = dates.astype(md.datetime.datetime)
    mp.plot(dates, profits, c='gray', label='Profits')
    gain_dates, gains = dates[profits > 0], \
        profits[profits > 0]
    mp.plot(gain_dates, gains, 'o', c='orangered',
            label='Gains')
    ave_gains = np.empty_like(gains)
    ave_gains.fill(
        gains.mean() if gains.size > 0 else 0)
    mp.plot(gain_dates, ave_gains, '--', c='orangered',
            linewidth=1, label='Average of Gains')
    loss_dates, losses = dates[profits < 0], \
        profits[profits < 0]
    mp.plot(loss_dates, losses, 'o', c='dodgerblue',
            label='Losses')
    ave_losses = np.empty_like(losses)
    ave_losses.fill(
        losses.mean() if losses.size > 0 else 0)
    mp.plot(loss_dates, ave_losses, '--', c='dodgerblue',
            linewidth=1, label='Average of Losses')
    mp.gcf().autofmt_xdate()
    mp.legend()


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    dates, opening_prices, highest_prices, \
        lowest_prices, closing_prices = read_data(
            'bhp.csv')
    buying_rate = 0.9985
    buying_rates = np.zeros_like(closing_prices)
    buying_rates.fill(buying_rate)
    dates, profits = calc_profits(
        dates, buying_rates, opening_prices,
        highest_prices, lowest_prices, closing_prices)
    init_chart(buying_rate, dates[0], dates[-1])
    draw_chart(dates, profits)
    show_chart()
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

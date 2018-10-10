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
    '''
    print(dates)
    print(opening_prices)
    print(highest_prices)
    print(lowest_prices)
    print(closing_prices)
    '''
    return dates, opening_prices, highest_prices, \
        lowest_prices, closing_prices


def init_chart(first_day, last_day):
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Candlestick Chart', fontsize=20)
    mp.xlabel('Trading Days From %s To %s' % (
        first_day.astype(md.datetime.datetime).strftime(
            '%d %b %Y'),
        last_day.astype(md.datetime.datetime).strftime(
            '%d %b %Y')), fontsize=14)
    mp.ylabel('Stock Price (USD) Of Apple Inc.',
              fontsize=14)
    ax = mp.gca()
    ax.xaxis.set_major_locator(
        md.WeekdayLocator(byweekday=md.MO))
    ax.xaxis.set_minor_locator(md.DayLocator())
    ax.xaxis.set_major_formatter(
        md.DateFormatter('%d %b %Y'))

    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_chart(dates, opening_prices, highest_prices,
               lowest_prices, closing_prices):
    dates = dates.astype(md.datetime.datetime)
    up = closing_prices - opening_prices >= 1e-2
    down = opening_prices - closing_prices >= 1e-2
    fc = np.zeros(dates.size, dtype='3f4')
    ec = np.zeros(dates.size, dtype='3f4')
    fc[up], fc[down] = (1, 1, 1), (0, 0.5, 0)
    ec[up], ec[down] = (1, 0, 0), (0, 0.5, 0)
    mp.bar(dates, highest_prices - lowest_prices, 0,
           lowest_prices, align='center', color=fc,
           edgecolor=ec)
    mp.bar(dates, closing_prices - opening_prices, 0.8,
           opening_prices, align='center', color=fc,
           edgecolor=ec)
    mp.gcf().autofmt_xdate()


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
            'aapl.csv')
    init_chart(dates[0], dates[-1])
    draw_chart(dates, opening_prices, highest_prices,
               lowest_prices, closing_prices)
    show_chart()
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

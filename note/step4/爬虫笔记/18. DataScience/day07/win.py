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
    dates, closing_prices = np.loadtxt(
        filename, delimiter=',', usecols=(1, 6),
        unpack=True, dtype=np.dtype('M8[D], f8'),
        converters={1: dmy2ymd})
    return dates, closing_prices


def calc_mas(win, N, closing_prices):
    weights = win(N) if win != np.kaiser else win(N, 0)
    weights /= weights.sum()
    print(weights)
    mas = np.convolve(closing_prices, weights, 'valid')
    return mas


def init_chart(first_day, last_day):
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Window Movine Average', fontsize=20)
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


def draw_closing_prices(dates, closing_prices):
    dates = dates.astype(md.datetime.datetime)
    mp.plot(dates, closing_prices, 'o-', c='lightgray',
            label='Closing Price')


def draw_mas(N, dates, nw_mas, bl_mas, bm_mas, hm_mas,
             hn_mas, ks_mas):
    dates = dates.astype(md.datetime.datetime)
    mp.plot(dates, nw_mas, label='MA-%d No Window' % N)
    mp.plot(dates, bl_mas, label='MA-%d Bartlett Window' % N)
    mp.plot(dates, bm_mas, label='MA-%d Blackman Window' % N)
    mp.plot(dates, hm_mas, label='MA-%d Hamming Window' % N)
    mp.plot(dates, hn_mas, label='MA-%d Hanning Window' % N)
    mp.plot(dates, ks_mas, label='MA-%d Kaiser Window' % N)

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
    dates, closing_prices = read_data('aapl.csv')
    N = 5
    nw_mas = calc_mas(np.ones, N, closing_prices)
    bl_mas = calc_mas(np.bartlett, N, closing_prices)
    bm_mas = calc_mas(np.blackman, N, closing_prices)
    hm_mas = calc_mas(np.hamming, N, closing_prices)
    hn_mas = calc_mas(np.hanning, N, closing_prices)
    ks_mas = calc_mas(np.kaiser, N, closing_prices)

    init_chart(dates[0], dates[-1])
    draw_closing_prices(dates, closing_prices)
    draw_mas(N, dates[N - 1:], nw_mas, bl_mas, bm_mas, hm_mas,
             hn_mas, ks_mas)
    show_chart()
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

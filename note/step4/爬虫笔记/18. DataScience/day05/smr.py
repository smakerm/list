import os
import sys
import warnings
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


def calc_returns(N, closing_prices):
    returns = np.diff(closing_prices) / closing_prices[:-1]
    weights = np.hanning(N)
    smr = np.convolve(weights, returns, 'valid')
    return returns, smr


def fit_polys(fit_x, fit_y, fit_d, poly_x):
    fit_p = np.polyfit(fit_x, fit_y, fit_d)
    poly_y = np.polyval(fit_p, poly_x)
    return poly_y


def find_inters(fit_x, fit_y1, fit_y2,
                fit_d, min_x, max_x):
    fit_p1 = np.polyfit(fit_x, fit_y1, fit_d)
    fit_p2 = np.polyfit(fit_x, fit_y2, fit_d)
    fit_p3 = np.polysub(fit_p1, fit_p2)
    roots = np.roots(fit_p3)
    reals = roots[np.isreal(roots)].real
    inters = []
    for real in reals:
        if min_x < real and real < max_x:
            inters.append([real,
                           np.polyval(fit_p1, real)])
    inters.sort()
    inters = np.array(inters)
    return inters


def init_chart(N, first_day, last_day):
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Smoothing Returns (%d Days)' % N, fontsize=20)
    mp.xlabel('Trading Days From %s To %s' % (
        first_day.astype(md.datetime.datetime).strftime(
            '%d %b %Y'),
        last_day.astype(md.datetime.datetime).strftime(
            '%d %b %Y')), fontsize=14)
    mp.ylabel('Returns Of Stock Price', fontsize=14)
    ax = mp.gca()
    ax.xaxis.set_major_locator(
        md.WeekdayLocator(byweekday=md.MO))
    ax.xaxis.set_minor_locator(md.DayLocator())
    ax.xaxis.set_major_formatter(
        md.DateFormatter('%d %b %Y'))

    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_returns(dates, bhp_returns, vale_returns):
    dates = dates.astype(md.datetime.datetime)
    mp.plot(dates, bhp_returns, '-', c='orangered',
            alpha=0.25, label='BHP Returns')
    mp.plot(dates, vale_returns, '-', c='dodgerblue',
            alpha=0.25, label='VALE Returns')


def draw_smrs(N, dates, bhp_smrs, vale_smrs):
    dates = dates.astype(md.datetime.datetime)
    mp.plot(dates, bhp_smrs, '-', c='orangered',
            alpha=0.75, label='BHP SMR-%d' % N)
    mp.plot(dates, vale_smrs, '-', c='dodgerblue',
            alpha=0.75, label='VALE SMR-%d)' % N)


def draw_polys(N, dates, bhp_polys, vale_polys, degree):
    dates = dates.astype(md.datetime.datetime)
    mp.plot(dates, bhp_polys, '-', c='orangered',
            label='BHP SMR-%d Polynomial (%d)' % (
                N, degree))
    mp.plot(dates, vale_polys, '-', c='dodgerblue',
            label='VALE SMR-%d Polynomal (%d)' % (
                N, degree))


def draw_inters(inters):
    dates, inters = np.hsplit(inters, 2)
    dates = dates.astype(int).astype(
        'M8[D]').astype(md.datetime.datetime)
    mp.scatter(dates, inters, marker='X', s=120,
               c='firebrick',
               label='Intersection of SMRs', zorder=3)

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
    warnings.filterwarnings('ignore',
                            category=np.RankWarning)
    dates, bhp_closing_prices = read_data('bhp.csv')
    dates, vale_closing_prices = read_data('vale.csv')
    N = 8
    bhp_returns, bhp_smrs = calc_returns(
        N, bhp_closing_prices)
    vale_returns, vale_smrs = calc_returns(
        N, vale_closing_prices)
    days = dates[N - 1:-1].astype(int)
    degree = 5
    bhp_ploys = fit_polys(days, bhp_smrs, degree, days)
    vale_ploys = fit_polys(days, vale_smrs, degree, days)
    inters = find_inters(days, bhp_smrs, vale_smrs,
                         degree, days[0], days[-1])
    init_chart(N, dates[0], dates[-2])
    draw_returns(dates[:-1], bhp_returns, vale_returns)
    draw_smrs(N, dates[N - 1:-1], bhp_smrs, vale_smrs)
    draw_polys(N, dates[N - 1:-1], bhp_ploys, vale_ploys,
               degree)
    draw_inters(inters)
    show_chart()
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

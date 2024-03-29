import os
import sys
import csv
import datetime as dt
import numpy as np


g_weekdays = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')


def dmy2weekday(dmy):
    return dt.datetime.strptime(
        str(dmy, encoding='utf-8'),
        '%d-%m-%Y').date().weekday()


def read_data(filename):
    weekdays, opening_prices, highest_prices, \
        lowest_prices, closing_prices = np.loadtxt(
            filename, delimiter=',', usecols=(1, 3, 4, 5, 6),
            unpack=True, converters={1: dmy2weekday})
    return weekdays[:16], opening_prices[:16], \
        highest_prices[:16], lowest_prices[:16], \
        closing_prices[:16]


def get_summary(
    week_indices, opening_prices, highest_prices,
        lowest_prices, closing_prices):
    opening_price = opening_prices[week_indices[0]]
    highest_price = np.max(
        np.take(highest_prices, week_indices))
    lowest_price = np.min(
        np.take(lowest_prices, week_indices))
    closing_price = closing_prices[week_indices[-1]]
    return opening_price, highest_price, lowest_price, \
        closing_price


def get_summaries(
        weekdays, opening_prices, highest_prices,
        lowest_prices, closing_prices):
    first = np.where(weekdays == 0)[0][0]
    last = np.where(weekdays == 4)[0][-1]
    indices = np.arange(first, last + 1)
    indices = np.split(indices, 3)
    summaries = np.apply_along_axis(
        get_summary, 1, indices, opening_prices,
        highest_prices, lowest_prices, closing_prices)
    return summaries


def save_summaries(summaries):
    filename = 'summary.csv'
    '''
    np.savetxt(filename, summaries, delimiter=',',
               fmt='%g')
    '''
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for summary in summaries:
            row = list(summary)
            row.insert(0, 'AAPL')
            writer.writerow(row)


def main(argc, argv, envp):
    weekdays, opening_prices, highest_prices, \
        lowest_prices, closing_prices = read_data(
            'aapl.csv')
    summaries = get_summaries(
        weekdays, opening_prices, highest_prices,
        lowest_prices, closing_prices)
    print(summaries)
    save_summaries(summaries)
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

import os
import sys
import platform
import numpy as np
import matplotlib.pyplot as mp


def game(rounds, principal):
    chips = np.zeros(rounds + 1)
    chips[0] = principal
    outcomes = np.random.binomial(9, 0.5, size=rounds)
    for i, outcome in enumerate(outcomes):
        if outcome < 5:
            chips[i + 1] = chips[i] - 1
        else:
            chips[i + 1] = chips[i] + 1
    return chips


def init_chart():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Binomial Distribution', fontsize=20)
    mp.xlabel('Round', fontsize=14)
    mp.ylabel('Chip', fontsize=14)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_chart(chips):
    p, h, l, b = 0, chips.argmax(), chips.argmin(), \
        chips.size - 1
    if chips[p] < chips[b]:
        color = 'orangered'
    elif chips[b] < chips[p]:
        color = 'limegreen'
    else:
        color = 'dodgerblue'
    mp.plot(chips, c=color, label='Chip')

    mp.axhline(y=chips[p], linestyle='--', color='deepskyblue')
    mp.axhline(y=chips[h], linestyle='--', color='crimson')
    mp.axhline(y=chips[l], linestyle='--', color='seagreen')
    mp.axhline(y=chips[b], linestyle='--', color='orange')

    mp.plot(p, chips[p], 'o', c='deepskyblue')
    mp.plot(h, chips[h], 'o', c='crimson')
    mp.plot(l, chips[l], 'o', c='seagreen')
    mp.plot(b, chips[b], 'o', c='orange')

    mp.legend()


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    chips = game(10000, 1000)
    init_chart()
    draw_chart(chips)
    show_chart()
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

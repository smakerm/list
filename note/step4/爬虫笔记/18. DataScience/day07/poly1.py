import os
import sys
import platform
import numpy as np
import matplotlib.pyplot as mp


def init_chart():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Polynomial Function', fontsize=20)
    mp.xlabel('x', fontsize=14)
    mp.ylabel('y', fontsize=14)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_chart(x, y):
    mp.plot(x, y, c='orangered', label='$y=x^3+2x^2+3x+4$')
    mp.legend()


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    x = np.linspace(-10, 10, 201)
    f = np.poly1d([1., 2., 3., 4.])
    y = f(x)
    init_chart()
    draw_chart(x, y)
    show_chart()
    return 0


if __name__ == '__main__':
    exit(main(len(sys.argv), sys.argv, os.environ))

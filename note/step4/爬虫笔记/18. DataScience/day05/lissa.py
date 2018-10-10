import os
import sys
import platform
import numpy as np
import matplotlib.pyplot as mp


def init_chart():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Lissajous', fontsize=20)
    mp.xlabel(r'$x=Asin(at+\frac{\pi}{2})$', fontsize=14)
    mp.ylabel(r'$y=Bsin(bt)$', fontsize=14)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def ufunc(A, a, B, b):
    def func(t):
        x = A * np.sin(a * t + np.pi / 2)
        y = B * np.sin(b * t)
        return x, y
    return np.frompyfunc(func, 1, 2)


def calc_lissa(A, a, B, b, t):
    x = A * np.sin(a * t + np.pi / 2)
    y = B * np.sin(b * t)
    return x, y


def draw_chart(x, y, c, A, a, B, b):
    mp.plot(x, y, c=c,
            label='A={},a={},B={},b={}'.format(A, a, B, b))
    mp.legend(loc=1)


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    t = np.linspace(-np.pi, np.pi, 201)
    init_chart()
    A, a, B, b = 10, 9, 5, 8
    #x, y = ufunc(A, a, B, b)(t)
    x, y = calc_lissa(A, a, B, b, t)
    draw_chart(x, y, 'bisque', A, a, B, b)
    A, a, B, b = 10, 1, 5, 1
    x, y = ufunc(A, a, B, b)(t)
    draw_chart(x, y, 'orangered', A, a, B, b)
    A, a, B, b = 10, 1, 5, 2
    x, y = ufunc(A, a, B, b)(t)
    draw_chart(x, y, 'limegreen', A, a, B, b)
    A, a, B, b = 10, 1, 5, 3
    x, y = ufunc(A, a, B, b)(t)
    draw_chart(x, y, 'dodgerblue', A, a, B, b)
    show_chart()
    return 0


if __name__ == '__main__':
    exit(main(len(sys.argv), sys.argv, os.environ))

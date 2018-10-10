import os
import sys
import platform
import numpy as np
import matplotlib.pyplot as mp


def init_chart():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Squarewaves', fontsize=20)
    mp.xlabel(r'$x\in[-\pi,\pi]$', fontsize=14)
    mp.ylabel(r'$y=\sum_{n=1}^N\frac'
              '{sin((2n-1)x)}{(2n-1\pi)}$', fontsize=14)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def ufunc(N):
    k = np.arange(1, 2 * N, 2)

    def func(x):
        return (np.sin(k * x) / k).sum() * 4 / np.pi
    return np.frompyfunc(func, 1, 1)


def draw_chart(x, y, c, N):
    mp.plot(x, y, c=c, label='N={}'.format(N))
    mp.legend(loc=4)


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    x = np.linspace(-np.pi, np.pi, 201)
    init_chart()
    N = 1
    y = ufunc(N)(x)
    draw_chart(x, y, 'bisque', N)
    N = 2
    y = ufunc(N)(x)
    draw_chart(x, y, 'orangered', N)
    N = 3
    y = ufunc(N)(x)
    draw_chart(x, y, 'limegreen', N)
    N = 1000
    y = ufunc(N)(x)
    draw_chart(x, y, 'dodgerblue', N)
    show_chart()
    return 0


if __name__ == '__main__':
    exit(main(len(sys.argv), sys.argv, os.environ))

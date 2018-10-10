import os
import sys
import platform
import numpy as np
import matplotlib.pyplot as mp


def init_poly():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.subplot(311)
    mp.title('Polynomial Function', fontsize=16)
    mp.xlabel('x', fontsize=12)
    mp.ylabel('y', fontsize=12)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_poly(x, y):
    mp.plot(x, y, 'o-', c='orangered', label='$y=x^3+2x^2+3x+4$')
    mp.legend()


def init_first():
    mp.subplot(312)
    mp.title('First Order Derivative', fontsize=16)
    mp.xlabel('x', fontsize=12)
    mp.ylabel("y'", fontsize=12)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_first(x, dy):
    mp.plot(x, dy, '>--', c='limegreen', label='y=dy/dx')
    mp.legend()


def init_second():
    mp.subplot(313)
    mp.title('Second Order Derivative', fontsize=16)
    mp.xlabel('x', fontsize=12)
    mp.ylabel('y"', fontsize=12)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_second(x, dy):
    mp.plot(x, dy, '^-.', c='dodgerblue',
            label='$y=d^2y/(dx)^2$')
    mp.legend()


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.tight_layout()
    mp.show()


def main(argc, argv, envp):
    x = np.linspace(-10, 10, 41)
    f = np.poly1d([1., 2., 3., 4.])
    y = f(x)
    df = f.deriv(m=1)
    dy = df(x)
    ddf = f.deriv(m=2)
    ddy = ddf(x)
    init_poly()
    draw_poly(x, y)
    init_first()
    draw_first(x, dy)
    init_second()
    draw_second(x, ddy)
    show_chart()
    return 0


if __name__ == '__main__':
    exit(main(len(sys.argv), sys.argv, os.environ))

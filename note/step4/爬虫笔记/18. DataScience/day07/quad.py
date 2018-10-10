import os
import sys
import platform
import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as mp
import matplotlib.patches as mc


def func_curve(x):
    y = 2 * x ** 2 + 3 * x + 4
    return y


def init_chart():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Integral', fontsize=20)
    mp.xlabel('x', fontsize=14)
    mp.ylabel('y', fontsize=14)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def auto_area(a, b):
    x = np.linspace(a, b, 1001)
    y = func_curve(x)
    mp.plot(x, y, c='red', linewidth=8, label='$y=2x^2+3x+4$')
    mp.legend()
    area = si.quad(func_curve, a, b)[0]
    return area


def manu_area(a, b):
    X = np.linspace(a, b, 1001)
    Y = func_curve(X)
    ax = mp.gca()
    area = 0
    for i, (x, y) in enumerate(zip(X[:-1], Y[:-1])):
        lb = [x, 0]
        lt = [x, y]
        rt = [X[i + 1], Y[i + 1]]
        rb = [X[i + 1], 0]
        ax.add_patch(mc.Polygon([lb, lt, rt, rb],
                                fc='skyblue', ec='dodgerblue'))
        h1 = np.abs(y)
        h2 = np.abs(Y[i + 1])
        w = np.abs(X[i + 1] - x)
        s = (h1 + h2) * w / 2
        area += s
    return area


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    a, b = -5, 5
    init_chart()
    print(auto_area(a, b))
    print(manu_area(a, b))
    show_chart()
    return 0


if __name__ == '__main__':
    exit(main(len(sys.argv), sys.argv, os.environ))

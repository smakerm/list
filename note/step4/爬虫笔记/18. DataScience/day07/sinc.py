import os
import sys
import platform
import numpy as np
import matplotlib.pyplot as mp
import mpl_toolkits.axes_grid1 as mg


def sinc(min, max, num):
    x = np.linspace(min, max, num)
    y = np.sinc(x)
    return x, y


def sinc2d(min, max, num):
    x = np.linspace(min, max, num)
    xy = np.outer(x, x)
    z = np.sinc(xy)
    return z


def init_sinc():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.subplot(121)
    mp.title('Sinc 1D', fontsize=20)
    mp.xlabel('x', fontsize=14)
    mp.ylabel('y=sinc(x)', fontsize=14)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_sinc(x, y):
    mp.scatter(x, y, c=y, cmap='jet', s=10, label='Sinc')
    mp.legend()


def init_sinc2d():
    mp.subplot(122)
    mp.title('Sinc 2D', fontsize=20)
    mp.xlabel('x', fontsize=14)
    mp.ylabel('y=sinc(x)', fontsize=14)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_sinc2d(z, min, max):
    im = mp.imshow(z, extent=(min, max, min, max), cmap='jet')
    dv = mg.make_axes_locatable(mp.gca())
    ca = dv.append_axes('right', '6%', pad='5%')
    cb = mp.colorbar(im, cax=ca)
    cb.set_label('z=sinc(xy)', fontsize=14)

    mp.legend()


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    min, max, num = -2.5, 2.5, 501
    x, y = sinc(min, max, num)
    z = sinc2d(min, max, num)
    init_sinc()
    draw_sinc(x, y)
    init_sinc2d()
    draw_sinc2d(z, min, max)
    show_chart()
    return 0


if __name__ == '__main__':
    exit(main(len(sys.argv), sys.argv, os.environ))

import os
import sys
import platform
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d


def sinc2d():
    x = np.linspace(-2.5, 2.5, 501)
    x, y = np.meshgrid(x, x)
    z = np.sinc(x * y)
    return x, y, z


def init_chart():
    ax = mp.gca(projection='3d')
    ax.set_title('3D Wireframe', fontsize=20)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)
    ax.set_zlabel('z=sinc(x,y)', fontsize=14)
    mp.tick_params(labelsize=10)


def draw_chart(x, y, z):
    mp.gca().plot_wireframe(x, y, z, rstride=20, cstride=20,
                            color='crimson')


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    x, y, z = sinc2d()
    init_chart()
    draw_chart(x, y, z)
    show_chart()
    return 0


if __name__ == '__main__':
    exit(main(len(sys.argv), sys.argv, os.environ))

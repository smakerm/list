import os
import sys
import platform
import numpy as np
import scipy.misc as sm
import scipy.ndimage as sn
import matplotlib.pyplot as mp


def load_image():
    return sm.ascent().astype(np.float32)


def median_filter(image):
    return sn.median_filter(image, (42, 42))


def rotate_image(image, angle=90):
    return sn.rotate(image, angle)


def prewitt_image(image):
    return sn.prewitt(image)


def init_chart(rcn, title):
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.subplot(rcn)
    mp.title(title, fontsize=16)
    mp.xlabel('Width', fontsize=12)
    mp.ylabel('Height', fontsize=12)
    ax = mp.gca()
    ax.xaxis.set_major_locator(mp.MultipleLocator(128))
    ax.xaxis.set_minor_locator(mp.MultipleLocator(32))
    ax.yaxis.set_major_locator(mp.MultipleLocator(128))
    ax.yaxis.set_minor_locator(mp.MultipleLocator(32))
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_chart(image):
    mp.imshow(image, cmap='gray')


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.tight_layout()
    mp.show()


def main(argc, argv, envp):
    original_image = load_image()
    median_filtered_image = median_filter(original_image)
    rotated_image = rotate_image(original_image)
    prewitted_image = prewitt_image(original_image)
    init_chart(221, 'Original Image')
    draw_chart(original_image)
    init_chart(222, 'Median Filtered Image')
    draw_chart(median_filtered_image)
    init_chart(223, 'Rotated Image')
    draw_chart(rotated_image)
    init_chart(224, 'Prewitted Image')
    draw_chart(prewitted_image)
    show_chart()
    return 0


if __name__ == '__main__':
    exit(main(len(sys.argv), sys.argv, os.environ))

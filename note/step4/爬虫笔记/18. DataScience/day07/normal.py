import os
import sys
import platform
import numpy as np
import matplotlib.pyplot as mp


def norm_rand(number_of_samples):
    samples = np.random.normal(size=number_of_samples)
    return samples


def init_chart():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Normal Distribution', fontsize=20)
    mp.xlabel('Samples', fontsize=14)
    mp.ylabel('Frequency', fontsize=14)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_chart(samples):
    n, bins, pathches = mp.hist(
        samples, int(np.sqrt(samples.size)), normed=True,
        facecolor='deepskyblue', edgecolor='steelblue',
        label='Occurrence')
    prob_dens = np.exp(-bins ** 2 / 2) / np.sqrt(2 * np.pi)
    mp.plot(bins, prob_dens, 'o-', c='orangered',
            label='Probability Density')

    mp.legend()


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    samples = norm_rand(10000)
    print(samples)
    init_chart()
    draw_chart(samples)
    show_chart()
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

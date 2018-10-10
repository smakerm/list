import os
import sys
import platform
import numpy as np
import matplotlib.pyplot as mp


def game(rounds):
    scores = np.zeros(rounds + 1)
    outcomes = np.random.hypergeometric(25, 1, 3, size=rounds)
    for i, outcome in enumerate(outcomes):
        if outcome == 3:
            scores[i + 1] = scores[i] + 1
        else:
            scores[i + 1] = scores[i] - 6
    return scores


def init_chart():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.title('Hypergeometric Distribution', fontsize=20)
    mp.xlabel('Round', fontsize=14)
    mp.ylabel('Score', fontsize=14)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_chart(scores):
    mp.plot(scores, 'o-', c='orangered', label='Score')

    mp.legend()


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    scores = game(100)
    init_chart()
    draw_chart(scores)
    show_chart()
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

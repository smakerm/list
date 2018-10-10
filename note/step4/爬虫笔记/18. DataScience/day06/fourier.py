import os
import sys
import platform
import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as mp


def gen_signals(n):
    times = np.linspace(0, 2 * np.pi, 201)
    sigs = np.zeros((n + 2, times.size))
    for i in range(1, n + 1):
        sigs[i, :] = 4 * np.sin((2 * i - 1) * times) / (
            (2 * i - 1) * np.pi)
        sigs[n + 1, :] += sigs[i, :]
    return times, sigs


def time2freq(sigs, dtime):
    freqs = nf.fftfreq(sigs.size, d=dtime)
    #freqs = np.linspace(-0.5 / dtime, 0.5 / dtime, sigs.size)
    #freqs = np.fft.fftshift(freqs)
    ffts = nf.fft(sigs)
    amps = np.abs(ffts)
    return freqs, ffts, amps


def freq2time(ffts):
    sigs = nf.ifft(ffts)
    return sigs.real


def init_signals():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.subplot(121)
    mp.title('Time Domain', fontsize=20)
    mp.xlabel('Time', fontsize=14)
    mp.ylabel('Signal', fontsize=14)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_signals(times, sigs):
    for i in range(sigs.shape[0]):
        if i == sigs.shape[0] - 1:
            mp.plot(times, sigs[i], label='{:.4f}'.format(
                1 / (2 * np.pi)))
        else:
            mp.plot(times, sigs[i], label='{:.4f}'.format(
                (2 * i - 1) / (2 * np.pi)))
    mp.legend()


def init_amplitudes():
    mp.subplot(122)
    mp.title('Frequence Domain', fontsize=20)
    mp.xlabel('Frequence', fontsize=14)
    mp.ylabel('Amplituyde', fontsize=14)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_signals(times, sigs):
    for i in range(sigs.shape[0]):
        if i == 0:
            mp.plot(times, sigs[i], label='{:.4f}'.format(
                1 / (2 * np.pi)), linewidth=6,
                c='palegreen')
        elif i == sigs.shape[0] - 1:
            mp.plot(times, sigs[i], label='{:.4f}'.format(
                1 / (2 * np.pi)))
        else:
            mp.plot(times, sigs[i], label='{:.4f}'.format(
                (2 * i - 1) / (2 * np.pi)))
    mp.legend()


def draw_amplitudes(freqs, amps):
    amps = amps[freqs >= 0]
    freqs = freqs[freqs >= 0]
    mp.plot(freqs, amps, c='orangered',
            label='Frequency Spectrum')
    mp.legend()


def show_chart():
    mng = mp.get_current_fig_manager()
    if 'Windows' in platform.system():
        mng.window.state('zoomed')
    else:
        mng.resize(*mng.window.maxsize())
    mp.show()


def main(argc, argv, envp):
    times, sigs = gen_signals(5)
    freqs, ffts, amps = time2freq(sigs[-1, :],
                                  times[1] - times[0])
    sigs[0, :] = freq2time(ffts)
    init_signals()
    draw_signals(times, sigs)
    init_amplitudes()
    draw_amplitudes(freqs, amps)
    show_chart()
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

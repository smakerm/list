import os
import sys
import platform
import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as mp


def noised_signals(duration, sample_rate, signal_freq):
    times = np.linspace(0, duration, duration * sample_rate)
    noised_sigs = np.sin(2 * np.pi * signal_freq * times) + \
        np.random.randn(times.size) / 2
    return times, noised_sigs


def time2freq(sigs, sample_rate):
    freqs = nf.fftfreq(sigs.size, d=1 / sample_rate)
    ffts = nf.fft(sigs)
    amps = np.abs(ffts)
    return freqs, ffts, amps


def freq2time(ffts):
    sigs = nf.ifft(ffts)
    return sigs.real


def filter(freqs, noised_ffts, noised_amps):
    fund_freq = np.abs(freqs[noised_amps.argmax()])
    high_freqs = np.where(np.abs(freqs) > fund_freq)
    filtered_ffts = noised_ffts.copy()
    filtered_ffts[high_freqs] = 0
    filtered_amps = noised_amps.copy()
    filtered_amps[high_freqs] = 0
    return fund_freq, filtered_ffts, filtered_amps


def init_noised_signals():
    mp.gcf().set_facecolor(np.ones(3) * 240 / 255)
    mp.subplot(221)
    mp.title('Noised Signal', fontsize=16)
    mp.xlabel('Time (sec)', fontsize=12)
    mp.ylabel('Signal', fontsize=12)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_noised_signals(times, noised_sigs):
    mp.plot(times, noised_sigs, c='orangered', label='Noised')
    mp.legend()


def init_noised_amplitudes():
    mp.subplot(222)
    mp.title('Noised Amplitude', fontsize=16)
    mp.xlabel('Frequency (Hz)', fontsize=12)
    mp.ylabel('Amplitude', fontsize=12)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_noised_amplitudes(freqs, noised_amps):
    noised_amps = noised_amps[freqs >= 0]
    freqs = freqs[freqs >= 0]
    mp.plot(freqs, noised_amps, c='limegreen', label='Noised')
    mp.legend()


def init_filtered_amplitudes():
    mp.subplot(224)
    mp.title('Filtered Amplitude', fontsize=16)
    mp.xlabel('Frequency (Hz)', fontsize=12)
    mp.ylabel('Amplitude', fontsize=12)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_filtered_amplitudes(freqs, filtered_amps):
    filtered_amps = filtered_amps[freqs >= 0]
    freqs = freqs[freqs >= 0]
    mp.plot(freqs, filtered_amps, c='dodgerblue',
            label='Filtered')
    mp.legend()


def init_filtered_signals():
    mp.subplot(223)
    mp.title('Filtered Signal', fontsize=16)
    mp.xlabel('Time (sec)', fontsize=12)
    mp.ylabel('Signal', fontsize=12)
    mp.tick_params(which='both', top=True, right=True,
                   labelright=True, labelsize=10)
    mp.grid(linestyle=':')


def draw_filtered_signals(times, filtered_sigs):
    mp.plot(times, filtered_sigs, c='hotpink',
            label='Filtered')
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
    duration = 5
    sample_rate = 50
    signal_freq = 0.4
    times, noised_sigs = noised_signals(
        duration, sample_rate, signal_freq)
    freqs, noised_ffts, noised_amps = time2freq(
        noised_sigs, sample_rate)
    fund_freq, filtered_ffts, filtered_amps = filter(
        freqs, noised_ffts, noised_amps)
    print('Founamental Frequency:', fund_freq)
    filtered_sigs = freq2time(filtered_ffts)
    init_noised_signals()
    draw_noised_signals(times, noised_sigs)
    init_noised_amplitudes()
    draw_noised_amplitudes(freqs, noised_amps)
    init_filtered_amplitudes()
    draw_filtered_amplitudes(freqs, filtered_amps)
    init_filtered_signals()
    draw_filtered_signals(times, filtered_sigs)
    show_chart()
    return 0

if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv, os.environ))

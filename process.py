import numpy as np
import librosa

def discrete_fourier(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            angle = 2j * np.pi * k * n / N
            X[k] += x[n] * np.exp(-angle)
    return X

def fft(a):
    n = len(a)
    if n == 1:
        return a

    theta = -2 * np.pi / n
    w = [np.complex(np.cos(theta * i), np.sin(theta * i)) for i in range(n)]

    Aeven = a[0::2]
    Aodd = a[1::2]

    Yeven = fft(Aeven)
    Yodd = fft(Aodd)

    Y = [0] * n
    for k in range(n // 2):
        w_yodd_k = w[k] * Yodd[k]
        yeven_k = Yeven[k]
        Y[k] = yeven_k + w_yodd_k
        Y[k + n // 2] = yeven_k - w_yodd_k

    return Y

def fftfreq(num_samples, sampling_rate):
    freq_bin_spacing = sampling_rate / num_samples
    
    if num_samples % 2 == 0:
        positive_freqs = np.arange(0, num_samples // 2, dtype=float)
        negative_freqs = np.arange(-num_samples // 2, 0, dtype=float)
    else:
        positive_freqs = np.arange(0, num_samples // 2 + 1, dtype=float)
        negative_freqs = np.arange(-(num_samples // 2), 0, dtype=float)
    
    freqs = np.concatenate((positive_freqs, negative_freqs))
    freqs *= freq_bin_spacing
    return freqs

def read_wav_file(file_path):
    signal, sample_rate = librosa.load(file_path, sr=None)
    return signal, sample_rate

import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
dt = 1/Fs
t = np.arange(0,2, dt)

f1, f2 = 30, 75
signal =(np.sin(2*np.pi*f1*t)+
         np.sin(2*np.pi*f2*t)+
         0.3*np.random.randn(len(t))
)

window_size = 200   
step_size = 100
window = np.hanning(window_size)

spectrogram = []

for start in range(0, len(signal)-window_size, step_size):
    chunk = signal[start:start+window_size]
    chunk_windowed = chunk * window

    fft_values = np.fft.fft(chunk_windowed)
    magnitude = np.abs(fft_values[:window_size//2])

    spectrogram.append(magnitude)

spectrogram = np.array(spectrogram).T

plt.imshow(spectrogram, aspect='auto', origin='lower',
           extent=[0, 2, 0, Fs/2])

plt.colorbar(label="Magnitude")
plt.xlabel("Time (sec)")
plt.ylabel("Frequency (Hz)")
plt.title("Spectrogram (From Scratch)")
plt.show()

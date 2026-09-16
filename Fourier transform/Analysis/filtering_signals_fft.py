import numpy as np
import matplotlib.pyplot as plt

Fs = 500
dt = 1/Fs
t = np.arange(0,1,dt)

f1 = 20
f2 = 50
f3 = 120

signal = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)+np.sin(2*np.pi*f3*t) + np.random.randn(len(t))

fft_values = np.fft.fft(signal)
N = len(fft_values)
freq = np.fft.fftfreq(N, dt)

#Manual filtering
mask = (np.abs(freq) >= 40) & (np.abs(freq) <= 60)
fft_values[~mask] = 0

filtered_signal = np.real(np.fft.ifft(fft_values))

magnitude = np.abs(fft_values)
positive = freq > 0

plt.title("Filtering signals using FFT and IFFT")
plt.plot(freq[positive], magnitude[positive])
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
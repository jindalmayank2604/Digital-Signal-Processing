import numpy as np
import matplotlib.pyplot as plt

Fs = 200
dt = 1/Fs
t = np.arange(0,1,dt)

f1 = 150
signal = np.sin(2*np.pi*f1*t) + np.random.randn(len(t))

fft_values = np.fft.fft(signal)
N = len(fft_values)
freq = np.fft.fftfreq(N, dt)


magnitude = np.abs(fft_values)
positive = freq > 0

plt.title("Aliasing signals using FFT and IFFT")
plt.plot(freq[positive], magnitude[positive])
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
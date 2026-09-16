import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
dt = 1/Fs
t = np.arange(0,1, dt)

f1 = 50
f2 = 55

signal = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)

fft_values = np.fft.fft(signal)
N = len(fft_values)
freq = np.fft.fftfreq(N, dt)
positive = freq >= 0
magnitude = np.abs(fft_values)

plt.title("FT Resolution to positive")
plt.plot(freq[positive], magnitude[positive])
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
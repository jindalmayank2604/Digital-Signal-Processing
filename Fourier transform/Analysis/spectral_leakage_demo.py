import numpy as np
import matplotlib.pyplot as plt

Fs = 1000 
dt = 1/Fs
t = np.arange(0,1,dt)

#Root cause of leakage
f1 = 50.5

signal = np.sin(2*np.pi*f1*t) 

fft_values = np.fft.fft(signal)
N = len(fft_values)

freq = np.fft.fftfreq(N, dt)
magnitude = np.abs(fft_values)

plt.title("Spectral Leakage")
plt.plot(freq, magnitude)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
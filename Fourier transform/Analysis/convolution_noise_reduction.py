import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
dt = 1/Fs
t = np.arange(0,1,dt)

signal = np.sin(2*np.pi*30*t) + 0.5*np.random.randn(len(t))

h = np.ones(5)/5

filtered_signal = np.convolve(signal, h, mode = "same")

plt.plot(t, signal, color='red', alpha = 0.3, label="Noisy")
plt.plot(t, filtered_signal,alpha = 1, label="Filtered")
plt.legend()
plt.grid(True)
plt.show()
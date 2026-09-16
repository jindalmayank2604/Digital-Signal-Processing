import numpy as np 
import matplotlib.pyplot as plt 

Fs = 1000
dt = 1/Fs
t = np.arange(0,2,dt)

f_start = 10
f_end = 150
T = 2

f_t = f_start + ((f_end-f_start)/T)*t
phase = 2*np.pi*np.cumsum(f_t)*dt

signal = np.sin(phase) 

window_size = 200
step_size = 100
window = np.hanning(window_size)

spectrogram = []

for start in range(0, len(t) - window_size, step_size):
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
plt.title("Linear Chirp Spectrogram")
plt.show()

import numpy as np 
import matplotlib.pyplot as plt 

Fs = 1000
dt = 1/Fs
t = np.arange(0,2,dt)

signal = np.zeros_like(t)

signal[t<1] = np.sin(2*np.pi*30*t[t<1])
signal[t>=1] = np.sin(2*np.pi*75*t[t>=1])
signal += 0.2*np.random.randn(len(t))


window_size = 400 
step_size = 100
window = np.hanning(window_size)

# Large window → sharp frequency line but blurry transition
# Small window → sharp transition but thick frequency line

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
plt.title("Time-Varying Spectrogram")
plt.show()
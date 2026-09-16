import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-np.pi , np.pi, 100)
y = np.zeros_like(x)
N1= 100
for n in range(1, N1+1, 2):
    sign = (-1)**((n-1)//2)
    y+= 8/np.pi**2 *sign* 1/n**2 * np.sin(n*x)


fft_values = np.fft.fft(y)
dx = x[1]-x[0]
N = len(y)
freq = np.fft.fftfreq(N, dx)
magnitude = np.abs(fft_values)

positive  = freq>= 0

plt.title("Triangle Wave Fourier Transform")
plt.plot(freq[positive], magnitude[positive])
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()


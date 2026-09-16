import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
# Sample frequency bangyi.. joki aage 1 sec me kitne signals mil re usko denote kregi

dt = 1/Fs
t = np.arange(0,1, dt)
#This line of code is making the values of t range from 0 to 1 with a gap of dt.

f = 50
signal = np.sin(2*np.pi*f*t)

fft_values = np.fft.fft(signal) 
#Returns an array with complex numbers where every index represents a freq

N = len(fft_values)
#Equals 1000 (sample)

freq = np.fft.fftfreq(N, dt)
'''
N x dt = 1s Gap, 
1s gap for 4 freq.. hence,
-2,-1,0,1

Ye basically humara x axis hogya
'''

magnitude = np.abs(fft_values)
#Strengh of the frequency from fft(signal) corresponding to the resulting indexes 

plt.title("Sin(50Hz) Fourier Transform")
plt.plot(freq, magnitude)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
import numpy as np

Fs = 1000
nyquist_freq = Fs/2

def hz_to_mel(f):
    return 2595 * np.log10(1 + f/700)
def mel_to_hz(m):
    return 700 * (10**(m/2595) - 1)

mel_min = hz_to_mel(0)
mel_max = hz_to_mel(nyquist_freq)

print("Mel(0 Hz):", mel_min)
print("Mel(500 Hz):", mel_max)

num_filter = 20

mel_points = np.linspace(mel_min, mel_max, num_filter +2)

hz_points = mel_to_hz(mel_points)

print("\nMel Points:")
print(mel_points)

print("\nConverted Back to Hz:")
print(hz_points)
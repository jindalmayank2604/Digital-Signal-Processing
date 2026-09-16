import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi * 4, np.pi * 4, 1000)
y=np.zeros_like(x)

N = int(input())

for n in range(1, N+1):
    sign = (-1) ** (n+1)
    y += 1/n * sign* np.sin(n*x)

plt.plot(x,y)
plt.title("Sawtooth Wave Series")
plt.grid(True)
plt.xlabel("ω")
plt.ylabel("f(ω)")
plt.show()
    
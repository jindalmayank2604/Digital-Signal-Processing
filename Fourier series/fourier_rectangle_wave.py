import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(-np.pi * 4, np.pi * 4, 1000)
y = np.zeros_like(x)
N = 100
for n in range(1, N+1, 2):
    y+= 4/np.pi * 1/n * np.sin(n*x)


plt.plot(x,y)
plt.title("Square Wave Series")
plt.grid(True)
plt.xlabel("ω")
plt.ylabel("f(ω)")
plt.show()
    
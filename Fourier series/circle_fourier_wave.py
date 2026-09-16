import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)

x = np.cos(t)
y = np.sin(t)


plt.plot(x,y)
plt.title("Circle Fourier Wave Series")
plt.grid(True)
plt.xlabel("ω")
plt.ylabel("f(ω)")
plt.show()
    
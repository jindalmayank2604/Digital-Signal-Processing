import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-np.pi * 4, np.pi * 4, 1000)
y = np.zeros_like(x)
N = int(input())
for n in range(1, N+1, 2):
    sign = (-1)**((n-1)/2)
    y+= 8/np.pi**2 *sign* 1/n**2 * np.sin(n*x)


plt.plot(x,y)
plt.title("Triangle Wave Series")
plt.grid(True)
plt.xlabel("ω")
plt.ylabel("f(ω)")
plt.show()
    
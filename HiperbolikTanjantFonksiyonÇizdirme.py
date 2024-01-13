import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,100)
tanh=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
plt.plot(x,tanh,color="magenta")
plt.title("Hiperbolik Tanjant")
plt.grid(True)
plt.axhline(0)
plt.axvline(0)
plt.show()

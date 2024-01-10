from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(-10,10,100)
sigm=1/ (1 + np.exp(-x))

plt.plot(x,sigm,label="Sigmoid func",color="magenta")
plt.grid(True)
plt.axhline(0)
plt.axvline(0)
plt.legend()
plt.show()
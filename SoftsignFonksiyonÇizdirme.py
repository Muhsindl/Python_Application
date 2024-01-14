import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,100)
y=x/(1+np.abs(x))

plt.axhline(0,color='red')
plt.axvline(0,color='red')
plt.plot(x,y,color="cyan")
plt.title("Softsign fonksiyonu")
plt.show()
import numpy as np
import matplotlib.pyplot as plt 
x=np.linspace(-10,10,100)
y=np.sin(x)/x
plt.axhline(0.4,color='red',alpha=0.3)
plt.axhline(0,color='red')
plt.axvline(0,color='red')
plt.plot(x,y,color="cyan")
plt.title("Sinc fonksiyonu")
plt.show()
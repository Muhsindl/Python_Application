import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(10,-10,10000) #10 ile -10 arasında 10.000 tane sayı oluşturur

#Formul
plt.plot(x, np.sqrt(1-(np.abs(x)-1)**2),'darkblue') #Koyu mavi renkli
plt.plot(x, np.arccos(1-np.abs(x))-np.pi,color="magenta") #Magenta renkli

plt.show()
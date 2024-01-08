import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0, 2 * np.pi, 200) #0,2pi aralığında 200 adet değer oluşturur
#formul
x = 16 * np.sin(t)**3 #formul
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

plt.plot(x,y,color="red") # renk belirler ve çizdirir
plt.title("Aşk") # Figure isim yazar
# plt.savefig("Aşk.png",dpi=300) #Kalbi png olarak kayıt eder
plt.show() # Figure ekranda gösterir 
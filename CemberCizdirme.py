import matplotlib.pyplot as plt
import numpy as np

# Çemberin merkez koordinatları
merkez_x = int(input("X için merkez girin: "))
merkez_y = int(input("Y için merkez girin: "))

# Çemberin yarıçapı
yaricap = int(input("Yarı çap giriniz: "))

theta = np.linspace(0, 2*np.pi, 1000)
x = merkez_x + yaricap * np.cos(theta)
y = merkez_y + yaricap * np.sin(theta)

plt.plot(x, y)
plt.title('Çember Çizimi')
plt.axis('equal') 

plt.show()
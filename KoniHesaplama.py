import numpy as np
r=int(input("Yarı çap: "))
h=int(input("Yükseklik giriniz: "))
# Hacim formulu
hacim=1/3*(np.pi*r**2*h)
#Yanal Yüzey Alan formulu
yanalAlan=np.pi*r*((r**2+h**2)**(1/2))

print("Hacim: ",hacim)
print("Yanal Yüzey Alanı:",yanalAlan)
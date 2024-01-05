import numpy as np
yariCap=int(input("Yarı çap giriniz: "))
cevre=2*np.pi*yariCap
alan=np.pi*(yariCap**2)
print("Çevresi: ",cevre,"\nAlan: ",alan)
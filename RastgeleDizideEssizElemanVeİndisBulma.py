import numpy as np

rng=np.random.default_rng() #Random generator tanımladık
dizi=rng.integers(0,100,50) #0-100 arası 50 tane tam sayılardan oluşan dizi oluşturduk

#Benzersiz elemanları ve indislerini bulduk
eleman,indis=np.unique(dizi,return_index=True)

#Benzersiz elemanları ve indislerini ekrana yazdırdık
print("Benzersiz eleman indisi: ",indis)
print("-*"*50)
print("Benzersiz elemanlar: ",eleman)

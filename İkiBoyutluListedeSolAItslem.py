import numpy as np
satır=int(input("Satır sayısı giriniz: "))
sutun=int(input("Sutun sayısı giriniz: "))
dizi=np.array([])

for i in range(satır):
    for j in range(sutun):
        n=int(input("Eleman giriniz: "))
        dizi=np.append(dizi,n)
dizi=dizi.reshape((satır,sutun))

eleman=int(input("Değiştirilecek eleman gir: "))
for i in range(satır):
    for j in range(sutun):
        if i>=j: # i>=j or i>j
            dizi[i][j]=eleman
print(dizi)

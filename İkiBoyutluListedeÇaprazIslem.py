import numpy as np
satır=int(input("Satır sayısı: "))
sutun=int(input("Sütun sayısı: "))
dizi=np.array([])

for i in range(satır):
    for j in range(sutun):
        n=int(input(f"Eleman giriniz Satır No: {i}, Sütun No: {j} "))
        dizi=np.append(dizi, n)
        
dizi=dizi.reshape((satır,sutun))
eleman=int(input("Değiştirilecek eleman giriniz: "))
for i in range(satır):
    for j in range(sutun):
        if i==j or j+i==sutun-1 and j+i==satır-1:
            dizi[i][j]=eleman
print(dizi)
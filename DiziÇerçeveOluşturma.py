import numpy as np
satır=int(input("Satır : "))
sutun=int(input("Sütun : "))
dizi=np.array([])
for i in range(satır):
    for j in range(sutun):
        nSütun=int(input("Eleman giriniz: "))
        dizi=np.append(dizi, nSütun)
dizi=dizi.reshape((satır,sutun))

diziDikeySıfır=np.zeros((satır+4,2))
diziYataySıfır=np.zeros((2,sutun))
birlestir=np.concatenate((diziYataySıfır,dizi,diziYataySıfır),axis=0)
sonuc=np.concatenate((diziDikeySıfır,birlestir,diziDikeySıfır),axis=1)
print(sonuc)
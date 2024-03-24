import numpy as np

boyut=int(input("Boyut giriniz: "))
diziGercek=[]
for i in range(boyut):
    sayi=int(input(f"{i+1}. Gerçek değer giriniz: "))
    diziGercek.append(sayi)
diziTahmin=[]
for i in range(boyut):
    sayi=int(input(f"{i+1}. Tahmin değer giriniz: "))
    diziTahmin.append(sayi)
diziLoss=[]
for i in range(boyut):
    loss=((diziGercek[i])*np.log(diziTahmin[i]))-((1-diziGercek[i])*(np.log(1-diziTahmin[i])))
    diziLoss.append(loss)
    
print("Kayıp Dizi",diziLoss)
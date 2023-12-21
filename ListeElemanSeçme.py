import numpy as np

dizi=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a=int(input("Elemanın satır aralık başlangıcı giriniz: "))
b=int(input("Elemanın satır aralık sonu giriniz: "))
c=int(input("Elemanın sütun aralık başlangıcı giriniz: "))
d=int(input("Elemanın sütun aralık sonu giriniz: "))
dizisec=dizi[a:b,c:d] #satırXsütun
print(b)

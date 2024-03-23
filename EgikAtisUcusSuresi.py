import numpy as np

h=int(input("İlk hız giriniz: "))
g=int(input("Yer çekimi ivmesi giriniz: "))
a=int(input("Açı giriniz: "))

def egikAtis(self,hiz=0,g=10,aci=45):
    formul=(2*hiz*np.sin(aci))/g
    return formul

print("Uçuş süresi: ",egikAtis(h,g,a))
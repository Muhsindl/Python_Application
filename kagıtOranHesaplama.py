#Kütüphane tanımlanıyor
import numpy as np
#...a3,a4,a5,a6,a7... için oranlar hep aynı kalır
# Formul Uzun Kenar= √2* Kısa Kenar
kısaKenar=float(input("Kısa kenar giriniz: "))
uzunKenar=np.sqrt(2)*kısaKenar
print("Kısa kenar: ",kısaKenar,"Uzun kenar: ",uzunKenar)
import numpy as np

deneme=int(input("Deneme sayısı giriniz: "))
sayiAltLimit=int(input("Alt limit giriniz: "))
sayiUstLimit=int(input("Üst limit giriniz: "))

#Alt limit ve üst limit arasında tam sayı oluşturuluyor rastgele olarak
tahminEdilecekSayi=np.random.randint(sayiAltLimit,sayiUstLimit,1)

#Tahmin işlemleri yapılıyor "deneme" sayısı boyutunda
for i in range(deneme):
    sayi=int(input("Sayı gir: "))
    if sayi< tahminEdilecekSayi:
        print("Daha yüksek gir")
    elif sayi==tahminEdilecekSayi:
        print("Doğru bildiniz")
        break
    elif sayi>tahminEdilecekSayi:
        print("Daha düşük gir")   
    if i==deneme-1:
        print("Hakkınız bitti")
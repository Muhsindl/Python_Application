import random

r=random.randint(1,10) #Tahmin edilecek aralığı giriniz.(Varsayılan 1-10 aralığı)

sayac=0
for i in range(1,4): # for range fonksiyonunun içine tahmin sayısı giriniz.(Varsayılan 3)
    n=int(input("Sayı giriniz: "))
    if n==r:
        print(i,"\'nci tahmin de doğru bildiniz")
        sayac=1
        break
if sayac==0:
    print("Tekrar deneyiniz")
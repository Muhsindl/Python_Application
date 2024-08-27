#Sayı alınması
k=int(input("Sayı giriniz: "))
elemanToplamı=str(k)

#Asal olup olmadığının kontrol edilmesi
sayac=0
for i in range(2,k):
    if k%i==0:
        sayac+=1

#Toplamlarının asal olup olmadığının kontrol edilmesi
toplam=0
for i in elemanToplamı:
    toplam+=int(i)    

for i in range(2,toplam):
    if toplam%i==0:
        sayac+=1

#Ekranda sonucun gösterilmesi
if (sayac==0):
    print("Sayı asal uyumludur")
else:
    print("Sayı asal uyumlu değildir")
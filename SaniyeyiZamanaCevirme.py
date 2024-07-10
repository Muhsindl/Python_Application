#Kullanıcıdan saniye değerinin alınması
sn=int(input("Saniye giriniz: "))
#Saat'e dönüştürülmesi
sa=sn//3600
#Kalan saniyelerin hesaplanması
sn=sn%3600
#Dakika'ya dönüştürülmesi
dk=sn//60
#Kalan saniyelerin hesaplanması
sn=sn%60
#Kullanıcıya gösterilmesi
print(f"Girilen zaman:\nSaat {sa} dakika {dk} saniye {sn}")
sayi=input("Sayı giriniz: ")
en_buyuk = '0'
for hane in sayi:
    if int(hane) > int(en_buyuk):
        en_buyuk= hane
print("En Büyük Sayı: ",en_buyuk)
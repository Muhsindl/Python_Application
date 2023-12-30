toplam=0
while True:
    sayi = int(input("Sayı giriniz:"))
    if sayi<0:
        break
    toplam+=sayi
print("Toplam:", toplam)
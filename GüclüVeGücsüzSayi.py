sayi=int(input("Sayı giriniz: "))
bolen=0
for i in range(2,sayi+1):
    if sayi%i==0:
        bolen+=i

if bolen>sayi:
    print("Güçlü sayıdır(Abundant)")
else:
    print("Güçsüz sayıdır(Deficient)")
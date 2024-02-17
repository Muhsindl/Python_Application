sayi=int(input("Sayı giriniz: "))
bolen=0
for i in range(2,sayi):
    if sayi%i==0:
        bolen+=i
if sayi>=bolen:
    print("Sayı büyüktür")
elif sayi==bolen:
    print("Sayı eşittir")
else:
    print("Sayı küçüktür")
sayi=int(input("Sayı gir: "))
fact=1
# Sayı 5'ten büyük ise faktöriyeli alınır
if sayi<5:
    for i in range(1,sayi+1):
        fact*=i
    print("Cevap: ",fact)
# Sayı 5'ten küçük ise bir küçüğünü alınır ve ikiye tam bölünür
else:
    result=(sayi-1)//2
    print("Cevap: ",result)
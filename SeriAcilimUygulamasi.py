x=int(input("X değeri giriniz: "))
k=int(input("e üssü kaça kadar seri açılımını hesaplayacaksınız: "))
#Faktoriyel hesaplama fonksiyonu
def faktoriyel(sayi):
    fact=1
    for i in range(1,sayi+1):
        fact*=i
    return fact
#e^x'in seri açılımı olan e^x=1+x+x^2/2!+x^3/3!+...+x^k/k! formulü kullanılarak hesaplama yapılır.
result=0
for i in range(k):
    result+=((x**i)/(faktoriyel(i)))
print(result)
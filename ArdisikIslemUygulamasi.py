#Kullanıcıdan x ve n değerlerini alarak fonksiyon sonucunu ekrana yazdırınız.
#Faktöriyel hesabı için fonksiyon yazınız.
def faktoriyel(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
#Kullanıcıdan x ve n değerlerini alalım.
basamak=int(input("Basamak giriniz: "))
x=int(input("X değeri giriniz: "))
sonuc=0
#Fonksiyonu hesaplayalım.
for i in range(basamak+1):
    sonuc+=(x**i)/faktoriyel(i)
#Sonucu ekrana yazdıralım.
print(f"Fonksiyon sonucu:{sonuc}")
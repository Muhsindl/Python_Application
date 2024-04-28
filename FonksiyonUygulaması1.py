# Kullanıcı tarafından girilen n değeri için aşağıdaki işlemi yapan bir program
# 1/1! + 1/2! + 1/3! + ... + 1/n! + n/(n!) + (n-1)/(n-1)! + ... + 1/1!

#Kullanıcıdan n değerini alalım
n=int(input("Değer giriniz: "))

#Faktoriyel hesaplamak için fonksiyon oluşturalım
def faktoriyel(sayi):
    if sayi<=1:
        return 1
    else:
        return sayi*faktoriyel(sayi-1)

#İşlemi yapalım
for i in range(1,n+1):
    hesap=(1/faktoriyel(i))+(i/faktoriyel(n-i))
print("Sonuç: ",hesap)
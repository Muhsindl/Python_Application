#X değeri ve seri açılım sınırı girilerek Taylor Seri Açılımı hesaplanır.
x = int(input("X değeri giriniz: "))
eleman = int(input("Seri açılım sınırı giriniz: "))

# Faktoriyel hesaplamak için fonksiyon tanımlanır
def fact(i):
    f = 1
    for j in range(1, i+1):
        f *= j
    return f

# Seri açılımı hesaplamak için döngü oluşturulur
basamak = 0
result = 1  # Başlangıç değeri 1
for i in range(eleman + 1):  # Seri açılım sınırını dahil etmek için eleman + 1
    if (i + 1) % 2 == 0:  # İkinci terimden itibaren çift indislerde işaret değişecek
        if basamak % 2 == 0:
            result += (x**i) / fact(i)
        else:
            result -= (x**i) / fact(i)
        basamak += 1

# Sonuç ekrana yazdırılır
print("Cevap:", result)

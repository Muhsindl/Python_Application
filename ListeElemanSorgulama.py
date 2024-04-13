#Dizi içindeki elemanların sorgulanması

dizi=[]
eleman=int(input("Eleman sayısı gir: "))
#Diziye eleman ekleme
for i in range(eleman):
    elem=int(input(f"{i+1}. elemanı giriniz: "))
    dizi.append(elem)

aranan=int(input("Sorgulanacak elemanı giriniz: "))
kucuk=0
buyuk=0
#Dizi içindeki elemanların sorgulanması
for i in dizi:
    if i>int(aranan):
        kucuk+=1
    if i<int(aranan):
        buyuk+=1
#Sonuçların ekrana yazdırılması
print(f"Büyük olduğu dizi eleman sayısı: {buyuk}\nKüçük olduğu dizi eleman sayısı: {kucuk}")
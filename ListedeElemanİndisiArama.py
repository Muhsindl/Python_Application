#Kullanıcıdan eleman sayısının alınması
sayi=int(input("Eleman sayısı giriniz: "))
dizi=[]
# Diziye eleman eklenmesi
for i in range(1,sayi+1):
    eleman=input(f"{i}. Eleman giriniz: ")
    dizi.append(eleman)
# Kullanıcıdan aranacak elemanın alınması
aranan=input("Aranacak elemanı giriniz: ")

# Elemanın dizide olup olmadığının kontrolü
if aranan in dizi:
    print(f"Aranan elemanın indis numarası: {dizi.index(aranan)}")
else:
    print("Eleman bulunamadı")

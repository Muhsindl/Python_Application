eleman=int(input("Eleman sayısı giriniz: "))
dizi=[]
#Elemanlar kullanıcıdan alınır
for i in range(eleman):
    ekle=int(input(f"{i}. Elemanı giriniz: "))
    dizi.append(ekle)
#Aranacak eleman kullanıcıdan alınır
arananEleman=int(input("Aranacak elemanı giriniz: "))
#Listede arama işlemi Sıralı aramaya (sequantial search) göre yapılır
for i in range(eleman):
    if arananEleman==dizi[i]:
        print(f"{i}.nci indiste yer almaktadır {arananEleman} sayısı.")
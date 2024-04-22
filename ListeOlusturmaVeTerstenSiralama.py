dizi1 = []
#Eleman sayısını kullanıcıdan alıyoruz
elemanSayisi=int(input("Eleman sayısı giriniz: "))
#Elemanları kullanıcıdan alıyoruz
for i in range(elemanSayisi):
    eleman=int(input(f"{i+1}. Elemanı giriniz: "))
    dizi1.append(eleman)
#Diziyi tersten sıralıyoruz
dizi2 = []
for j in range(len(dizi1) - 1, -1, -1):
    dizi2.append(dizi1[j])
#Sonuçları ekrana yazdırıyoruz
print("\nDizi: ",dizi1)
print("\nTers Sıralanmış Dizi:", dizi2)

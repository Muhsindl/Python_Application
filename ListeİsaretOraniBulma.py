# Kullanıcıdan alınan eleman sayısına göre bir dizi oluşturun ve bu dizideki pozitif, negatif ve sıfır elemanların oranlarını bulunuz.
elemanSayisi=int(input("Eleman sayısı giriniz: "))
dizi=[]
#Dizi oluşturma
for i in range(elemanSayisi):
    eleman=int(input(f"{i+1}. elemanı giriniz: "))
    dizi.append(eleman)

pozitifSayac=0
negatifSayac=0
sayac=0
#Dizi içindeki elemanların oranlarını bulma
for i in dizi:
    if i>0:
        pozitifSayac+=1
    elif i<0:
        negatifSayac+=1
    else:
        sayac+=1
#Oranlarını hesaplama
pozitifOran=pozitifSayac/len(dizi)
negatifOran=negatifSayac/len(dizi)
oran=sayac/len(dizi)
#Sonuçları ekrana yazdırma
print(f"Dizi Oranları:\n Pozitif Oran:{pozitifOran}\n Negatif Oranı:{negatifOran}\n Sıfır Oranı:{oran}")
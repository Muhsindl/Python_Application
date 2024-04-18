metin=input("Cümle giriniz: ")
#Sesli harfler: a,e,ı,i,o,ö,u,ü
sesli=["a","e","ı","i","o","ö","u","ü"]
sayac=0
#Metindeki sesli harfleri say
for i in range(len(metin)):
    for j in range(len(sesli)):
        if metin[i]==sesli[j]:
            sayac+=1
#Sesli harf oranını hesapla
oran=sayac/len(metin)
#Sonucu ekrana yazdır
print("Metinde bulunan sesli harf oranı: {}".format(oran))
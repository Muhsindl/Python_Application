#Eleman sayısını ve elemanları kullanıcıdan alarak varyansı hesaplayan uygulama
elemanSayisi=int(input("Eleman sayısı giriniz: "))
sayiDizisi=[]
toplam=0
ort=0
#varyans hesaplama formülü: varyans=((toplam-ort)**2)/elemanSayisi
for i in range(elemanSayisi):
    eleman=int(input(f"{i+1}. elemanı giriniz: "))
    sayiDizisi.append(eleman)
    toplam+=sayiDizisi[i]
ort=toplam/elemanSayisi
varyans=((toplam-ort)**2)/elemanSayisi
#varyansı ekrana yazdırma
print("Varyans sonucu: ",varyans)
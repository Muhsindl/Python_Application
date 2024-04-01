#Fonksiyonlar ile ortalama hesaplama
def hesaplaOrt(*sayi):
    dizi=[]
    for i in sayi:
        dizi.append(i)
        
    toplam=0
    minim=dizi[0]
    maxim=dizi[0]
    #Dizi içindeki sayıları toplama ve en büyük en küçük sayıları bulma
    for i in range(len(dizi)):
        toplam+=dizi[i]
        if (dizi[i]<minim):
            minim=dizi[i]
        if (dizi[i]>maxim):
            maxim=dizi[i]
    #Ortalama hesaplama
    MaxMinOrtalama=(maxim+minim)/2
    ortalama=toplam/len(dizi)
    fark=MaxMinOrtalama-ortalama
    return dizi,ortalama,MaxMinOrtalama,fark

#Fonksiyonu çağırma
d,o,m,f=hesaplaOrt(1,2,31,41,51,61,71,8,9)
#Sonuçları ekrana yazdırma
print(f"{d} dizisi için;\n Ortalama: {o}\n En büyük ve En küçük sayı ortalaması: {m}\n Genel Ortlamanın En Büyük En Küçük Sayı Ortalaması ile Farkı: {f}")
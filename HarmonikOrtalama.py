#Fonksiyonumuz sınırsız sayıda parametre alır ve bu parametrelerin harmonik ortalamasını döndürür.
def harmonic(*sayi):
    toplam=0
    altIslem=0
    dizi=list(sayi) #Tuple tipinde alınan parametreleri listeye çeviriyoruz.
    #Gerekli işlemleri yapıyoruz.
    for i in range(len(dizi)):
        altIslem+=(1/dizi[i])
    toplam=len(dizi)/altIslem
    return toplam#Fonksiyonun döndürdüğü değer.

#Fonksiyonu çağırıyoruz.
#Örnek
harmonic(1,2,3,4,5,6,7,8,9,10)
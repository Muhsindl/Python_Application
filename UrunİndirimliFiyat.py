urunfiyat=int(input("Ürün fiyatı giriniz: "))
indirim=int(input("inirim oranı: "))

def hesapla(fiyat,ind):
    ucret=0
    indirimfiyat=fiyat*(ind*0.01)
    ucret=fiyat-indirimfiyat
    return ucret

print(hesapla(urunfiyat,indirim))
#Sınıf oluşturarak apartman kira fiyatı hesaplama
class apartman(object):
    def __init__(self, fiyat, enflasyoniy,yil):
        self.yil=yil
        self.fiyat = fiyat
        self.enflasyon = enflasyon
    def zamYap(self):
        if self.yil < 5:
            self.fiyat = self.fiyat + self.enflasyon * 50
        elif self.yil < 10:
            self.fiyat = self.fiyat + self.enflasyon * 35
        else:
            self.zamliFiyat = self.fiyat + self.enflasyon * 25
        return self.fiyat
    def zamliFiyatGoster(self):
        return self.fiyat

#Ana program
apartFiyat=int(input("Aparman Kira Fiyatı giriniz: "))
enflasyon=int(input("Yıla ait enflasyon giriniz: "))
yil=int(input("Apartman kaç yıllık  giriniz: "))

#Sınıfı çağırma
apart1 = apartman(apartFiyat, enflasyon,yil)

#Sonuçları ekrana yazdırma
print("Zamsız normal fiyatı: ",apart1.zamliFiyatGoster())
#Zam yapma fonksiyonunu çağırma
apart1.zamYap()
#Zamlı fiyatı ekrana yazdırma
print(f"Belirtilen {yil} bina yaşı için girilen {enflasyon} oranında zam yapılmıştır: ",apart1.zamliFiyatGoster())

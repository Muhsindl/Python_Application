class VKISorgu:
    # Kişi bilgilerini başlatıyoruz
    def __init__(self, isim, kilo, uzunluk):
        self.isim = isim
        self.kilo = kilo
        self.uzunluk = uzunluk
    # VKİ hesaplama formülü
    def vkiHesaplama(self):
        return self.kilo / ((self.uzunluk / 100) ** 2)
    
    def vkiKategori(self):
        # VKİ'ye göre kategori belirleme
        vki = self.vkiHesaplama()
        if vki < 18.5:
            return "Zayıf"
        elif 18.5 <= vki <= 24.9:
            return "Normal"
        elif 25 <= vki <= 29.9:
            return "Fazla Kilolu"
        else:
            return "Aşırı Kilolu"

def kisiGirisAl():
    # Kullanıcıdan kişi bilgisi alıyoruz
    isim = input("Kişinin adı: ")
    kilo = float(input("Kilo (kg): "))
    uzunluk = float(input("Boy (cm): "))
    return VKISorgu(isim, kilo, uzunluk)

def vkiKategoriYazdir(kisilerListesi):
    # Kişileri ve VKİ kategorilerini ekrana yazdırma
    for kisi in kisilerListesi:
        kategori = kisi.vkiKategori()
        print(f"{kisi.isim}: {kategori} (VKİ: {kisi.vkiHesaplama():.2f})")

def main():
    kisilerListesi = []
    kisiSayisi = int(input("Kaç kişi gireceksiniz? "))
    
    # Kullanıcıdan belirtilen sayıda kişi bilgisi alıyoruz
    for i in range(kisiSayisi):
        kisi = kisiGirisAl()
        kisilerListesi.append(kisi)
    
    # Kategorilere göre kişileri yazdırıyoruz
    vkiKategoriYazdir(kisilerListesi)

# Programı çalıştırmak için ana fonksiyon
if __name__ == "__main__":
    main()

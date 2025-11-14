# Kisi sınıfı oluşturulur (isim ve e-posta bilgileri tutulur)
class Kisi:
    def __init__(self, isim, eposta="muhsindolu06@gmail.com"):
        self.isim = isim
        self.eposta = eposta

    # E-posta domain'ini güncelleyen metot
    def epostaGuncelleme(self, yeniAdres):
        eskiAdres = self.eposta.split("@")[1]
        self.eposta = self.eposta.replace(eskiAdres, yeniAdres)


# Ogrenci sınıfı (Kisi'den türetilmiş)
class Ogrenci(Kisi):
    def __init__(self, isim, id, kredi, eposta="muhsindolu06@gmail.com"):
        super().__init__(isim, eposta)
        self.id = id
        self.kredi = kredi


# Ogretmen sınıfı (Kisi'den türetilmiş)
class Ogretmen(Kisi):
    def __init__(self, isim, odaNo, egitimYili, eposta="muhsindolu06@gmail.com"):
        super().__init__(isim, eposta)
        self.odaNo = odaNo
        self.egitimYili = egitimYili


if __name__ == "__main__":
    # Öğrenci Bilgileri
    isim = input("Öğrenci İsmi: ")
    eposta = input("Öğrenci E-posta (Varsayılan: muhsindolu06@gmail.com): ") or "muhsindolu06@gmail.com"
    id = int(input("Öğrenci ID: "))
    kredi = int(input("Öğrenci Kredi: "))

    ogr1 = Ogrenci(isim, id, kredi, eposta)

    # Domain güncelleme
    if input("Öğrenci e-posta domainini güncellemek ister misiniz? (Evet/Hayır): ").lower() == "evet":
        yeniDomain = input("Yeni domain: ")
        ogr1.epostaGuncelleme(yeniDomain)

    print("Öğrenci E-postası:", ogr1.eposta)

    # Öğretmen Bilgileri
    isimOgretmen = input("Öğretmen İsmi: ")
    epostaOgretmen = input("Öğretmen E-posta (Varsayılan: muhsindolu06@gmail.com): ") or "muhsindolu06@gmail.com"
    odaNo = input("Öğretmen Oda No: ")
    egitimYili = input("Öğretmen Eğitim Yılı: ")

    ogrtmn1 = Ogretmen(isimOgretmen, odaNo, egitimYili, epostaOgretmen)

    # Domain güncelleme
    if input("Öğretmen e-posta domainini güncellemek ister misiniz? (Evet/Hayır): ").lower() == "evet":
        yeniDomainOgretmen = input("Yeni domain: ")
        ogrtmn1.epostaGuncelleme(yeniDomainOgretmen)

    print("Öğretmen E-postası:", ogrtmn1.eposta)

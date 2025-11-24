# Kisi temel sınıfı
class Kisi:
    def __init__(self, isim, eposta):
        self.isim = isim
        self.eposta = eposta

    # Alan adını (domain) günceller
    def epostaGuncelleme(self, yeniAdres):
        eskiAdres = self.eposta.split("@")[1]
        self.eposta = self.eposta.replace(eskiAdres, yeniAdres)


# Öğrenci sınıfı
class Ogrenci(Kisi):
    def __init__(self, isim, eposta, id, kredi):
        super().__init__(isim, eposta)
        self.id = id
        self.kredi = kredi


# Öğretmen sınıfı
class Ogretmen(Kisi):
    def __init__(self, isim, eposta, odaNo, egitimYili):
        super().__init__(isim, eposta)
        self.odaNo = odaNo
        self.egitimYili = egitimYili


if __name__ == "__main__":

    # --- Dinamik Öğrenci Girişi ---
    ogrenci_listesi = []
    ogr_sayisi = int(input("Kaç öğrenci gireceksiniz? "))
    ogr_domain = input("Tüm öğrenciler için yeni e-posta domaini: ")

    for i in range(ogr_sayisi):
        print(f"\n{i+1}. Öğrenci Bilgileri")
        isim = input("İsim: ")
        eposta = input("E-posta: ")
        id = int(input("ID: "))
        kredi = int(input("Kredi: "))

        ogr = Ogrenci(isim, eposta, id, kredi)
        ogr.epostaGuncelleme(ogr_domain)
        ogrenci_listesi.append(ogr)

    # --- Dinamik Öğretmen Girişi ---
    ogretmen_listesi = []
    ogretmen_sayisi = int(input("\nKaç öğretmen gireceksiniz? "))
    ogretmen_domain = input("Tüm öğretmenler için yeni e-posta domaini: ")

    for i in range(ogretmen_sayisi):
        print(f"\n{i+1}. Öğretmen Bilgileri")
        isim = input("İsim: ")
        eposta = input("E-posta: ")
        odaNo = int(input("Oda No: "))
        egitimYili = int(input("Eğitim Yılı: "))

        ogretmen = Ogretmen(isim, eposta, odaNo, egitimYili)
        ogretmen.epostaGuncelleme(ogretmen_domain)
        ogretmen_listesi.append(ogretmen)

    # --- Sonuçları Yazdır ---
    print("\n--- Güncellenmiş Öğrenci E-postaları ---")
    for ogr in ogrenci_listesi:
        print(f"{ogr.isim} -> {ogr.eposta}")

    print("\n--- Güncellenmiş Öğretmen E-postaları ---")
    for ogretmen in ogretmen_listesi:
        print(f"{ogretmen.isim} -> {ogretmen.eposta}")

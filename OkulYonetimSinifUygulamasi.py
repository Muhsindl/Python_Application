class Person:
    def __init__(self, ad, soyad, tcKimlik):
        self.__ad = ad
        self.__soyad = soyad
        self.__tcKimlik = tcKimlik
    
    # Getter ve Setter metodları
    @property
    def ad(self):
        return self.__ad
    @ad.setter
    def ad(self, ad):
        self.__ad = ad
    
    @property
    def soyad(self):
        return self.__soyad
    @soyad.setter
    def soyad(self, soyad):
        self.__soyad = soyad
    
    @property
    def tcKimlik(self):
        return self.__tcKimlik
    @tcKimlik.setter
    def tcKimlik(self, tcKimlik):
        self.__tcKimlik = tcKimlik

    def display_info(self):
        print(f"İsim: {self.__ad}\nSoyisim: {self.__soyad}\nT.C.: {self.__tcKimlik}")

#=================================================================================================
class Student(Person):
    def __init__(self, ad, soyad, tcKimlik, ogrNo, notOrt):
        super().__init__(ad, soyad, tcKimlik)
        self.ogrNo = ogrNo
        # Not ortalamasını setter üzerinden geçirerek kontrolü sağlıyoruz
        self.notOrt = notOrt 

    @property
    def notOrt(self):
        return self.__notOrt

    @notOrt.setter
    def notOrt(self, deger):
        if 0 <= deger <= 4:
            self.__notOrt = deger
        else:
            print("UYARI: Not ortalaması 0-4 aralığında olmalı! (0 olarak atandı)")
            self.__notOrt = 0

    def display_info(self):
        print(f"İsim: {self.ad}\nSoyisim: {self.soyad}\nT.C.: {self.tcKimlik}\nÖğrenci No: {self.ogrNo}\nNot Ortalaması: {self.notOrt}")

#=================================================================================================
class Teacher(Person):
    def __init__(self, ad, soyad, tcKimlik, maas):
        super().__init__(ad, soyad, tcKimlik)
        self.maas = maas

    @property
    def maas(self):
        return self.__maas

    @maas.setter
    def maas(self, maas):
        if maas > 0:
            self.__maas = maas
        else:
            print("UYARI: Maaş 0'dan büyük olmalı!")
            self.__maas = 0

    def display_info(self):
        print(f"İsim: {self.ad}\nSoyisim: {self.soyad}\nT.C.: {self.tcKimlik}\nMaaş: {self.__maas}")

#=================================================================================================
# GİRİŞ BÖLÜMÜ
#=================================================================================================

kayitlar = [] # Girilen kişileri tutacak liste

while True:
    print("\n" + "="*30)
    secim = input("Kimi eklemek istersiniz?\n[O]ğrenci, [Og]retmen, [C]ıkış: ").lower()

    if secim == 'c':
        print("Çıkış yapılıyor...")
        break

    elif secim in ['o', 'og']:
        # Ortak verileri al
        try:
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            tc = input("TC Kimlik: ")

            if secim == 'o': # Öğrenci Girişi
                no = input("Öğrenci No: ")
                ort = float(input("Not Ortalaması (0-4): "))
                yeni_kisi = Student(ad, soyad, tc, no, ort)
            
            elif secim == 'og': # Öğretmen Girişi
                maas = float(input("Maaş: "))
                yeni_kisi = Teacher(ad, soyad, tc, maas)

            kayitlar.append(yeni_kisi)
            print("-> Kişi başarıyla eklendi!")

        except ValueError:
            print("HATA: Lütfen sayısal değerleri doğru giriniz!")
    else:
        print("Geçersiz seçim!")

# Tüm kayıtları yazdırma
print("\n" + "#"*20 + " LİSTE SONUCU " + "#"*20)
if not kayitlar:
    print("Hiç kayıt girilmedi.")
else:
    for kisi in kayitlar:
        print("-" * 20)
        kisi.display_info()

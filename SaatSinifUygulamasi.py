import time  # time modülünü içe aktarıyoruz

# Saaat sınıfı ile zaman hesaplama yapıyoruz
class Saat:
    def __init__(self, saat, dakika, saniye):
        self.saat = saat
        self.dakika = dakika
        self.saniye = saniye
    
    def zamanHesapla(self):
        self.saniye += 1
        if self.saniye == 60:
            self.saniye = 0
            self.dakika += 1
        if self.dakika == 60:
            self.dakika = 0
            self.saat += 1
        if self.saat == 24:
            self.saat = 0
        
        # Saat, dakika ve saniye iki haneli olarak yazdırılıyor
        print(f"{self.saat:02}:{self.dakika:02}:{self.saniye:02}")

# Kullanıcıdan saat, dakika ve saniye değerlerini alıyoruz
saat = int(input("Saat girin (0-23): "))
dakika = int(input("Dakika girin (0-59): "))
saniye = int(input("Saniye girin (0-59): "))

s1 = Saat(saat, dakika, saniye)  # Saat sınıfından bir nesne oluşturuyoruz

while True:
    s1.zamanHesapla()  # Zamanı hesapla ve yazdır
    time.sleep(1)  # 1 saniye bekleyip bir sonraki adıma geç

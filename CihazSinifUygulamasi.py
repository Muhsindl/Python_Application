class Cihaz:
    def __init__(self, ad, tuketim):
        self.ad = ad
        self.tuketim = tuketim

    def calistir(self):
        print(f"{self.ad} cihazı çalıştı.")

class CamasirMakinesi(Cihaz):
    def __init__(self, ad, tuketim):
        super().__init__(ad, tuketim)
    
    def yika(self):
        print(f"{self.ad} çamaşır yıkıyor.")

class BulasikMakinesi(Cihaz):
    def __init__(self, ad, tuketim):
        super().__init__(ad, tuketim)

    def yika(self):
        print(f"{self.ad} bulaşık yıkıyor.")

def cihaz_sec():
    print("Lütfen bir cihaz seçin:")
    print("1 - Çamaşır Makinesi")
    print("2 - Bulaşık Makinesi")
    secim = input("Seçiminizi yapın (1 veya 2): ")

    if secim == "1":
        ad = input("Çamaşır Makinesinin adını girin: ")
        tuketim = float(input("Çamaşır Makinesinin enerji tüketimini girin (kWh): "))
        return CamasirMakinesi(ad, tuketim)
    elif secim == "2":
        ad = input("Bulaşık Makinesinin adını girin: ")
        tuketim = float(input("Bulaşık Makinesinin enerji tüketimini girin (kWh): "))
        return BulasikMakinesi(ad, tuketim)
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")
        return cihaz_sec()

def main():
    cihaz = cihaz_sec()
    cihaz.calistir()

    if isinstance(cihaz, CamasirMakinesi):
        cihaz.yika()
    elif isinstance(cihaz, BulasikMakinesi):
        cihaz.yika()

if __name__ == "__main__":
    main()

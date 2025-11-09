class Dikdortgen:
    def __init__(self, sol_ust: tuple, sag_alt: tuple):
        self.sol_ust = sol_ust
        self.sag_alt = sag_alt
        self.genislik = sag_alt[0] - sol_ust[0]
        self.yukseklik = sol_ust[1] - sag_alt[1]

    def alan(self):
        return self.genislik * self.yukseklik

    def cevre(self):
        return 2 * (self.genislik + self.yukseklik)

    def oteleme(self, x_ot, y_ot):
        self.sol_ust = (self.sol_ust[0] + x_ot, self.sol_ust[1] + y_ot)
        self.sag_alt = (self.sag_alt[0] + x_ot, self.sag_alt[1] + y_ot)
        print(f"Ötelenmiş koordinatlar -> Sol Üst: {self.sol_ust}, Sağ Alt: {self.sag_alt}")

if __name__=="__main__":
    # --- Kullanıcıdan giriş alınır ---
    print("Dikdörtgen oluşturmak için köşe koordinatlarını giriniz:")
    
    x1 = int(input("Sol üst köşe X: "))
    y1 = int(input("Sol üst köşe Y: "))
    
    x2 = int(input("Sağ alt köşe X: "))
    y2 = int(input("Sağ alt köşe Y: "))
    
    # Dikdörtgen oluştur
    d1 = Dikdortgen((x1, y1), (x2, y2))
    
    # Alan ve çevreyi yazdır
    print(f"\nDikdörtgenin alanı: {d1.alan()}")
    print(f"Dikdörtgenin çevresi: {d1.cevre()}")
    
    # Öteleme isteği
    secim = bool(int(input("\nDikdörtgeni ötelemek ister misiniz? (1: Evet / 0: Hayır): ")))

    
    if secim:
        x_ot = int(input("X ekseninde kaç birim ötelemek istersiniz: "))
        y_ot = int(input("Y ekseninde kaç birim ötelemek istersiniz: "))
        d1.oteleme(x_ot, y_ot)
    else:
        print("Dikdörtgen ötelenmedi.")
    
    print("\nİşlem tamamlandı.")

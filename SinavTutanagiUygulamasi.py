class SinavTutanagi:
    def __init__(self, kisi, puan):
        self.kisi = kisi
        self.puan = puan

if __name__ == "__main__":
    
    # Kullanıcıdan mevcut ve geçme sınır notunun alınması
    sinifMevcut = int(input("Sınıf mevcudu kaç kişi: "))
    gecmeNotu = int(input("Geçme sınırı kaç: "))

    sinavlarDizisi = []

    # Kullanıcıdan her öğrenci için ad ve puan alma
    for i in range(sinifMevcut):
        kisi = input(f"{i+1}. öğrencinin adını girin: ")
        puan = int(input(f"{kisi} için puanı girin: "))
        sinavlarDizisi.append(SinavTutanagi(kisi, puan))  # Yeni SinavTutanagi nesnesini listeye ekliyoruz
    
    # Sınavı geçip geçmediğini kontrol eden fonksiyon
    def sınavGectiMi(sinavlar, limitNot):
        gecen = []
        kalan = []
        
        for sinav in sinavlar:
            if sinav.puan >= limitNot:
                gecen.append(sinav.kisi)
            else:
                kalan.append(sinav.kisi)
        
        return gecen, kalan

    # Sonuçları al
    gecenler, kalanlar = sınavGectiMi(sinavlarDizisi, gecmeNotu)

    # Sonuçları yazdır
    print("============================")
    print(f"Sınavı geçenler: {gecenler}")
    print(f"Sınavı geçemeyenler: {kalanlar}")

class SinavRaporu:
    def __init__(self, isim, ogrNot):
        # Öğrencinin ismi ve notu
        self.isim = isim
        self.ogrNot = ogrNot

#------------------------------------------------------
def gecti(sinavRap:list, limit:int):
    # Sınav raporu listesini alır ve geçme limitine göre geçen öğrencileri döndürür
    sinavDizisi = sinavRap
    gecenler = []  # Geçen öğrencilerin isimlerini tutacak liste
    gecemeyenler = []  # Geçemeyen öğrencilerin isimlerini tutacak liste
    for sinav in sinavDizisi:
        if sinav.ogrNot >= limit:
            gecenler.append(sinav.isim)
        else:
            gecemeyenler.append(sinav.isim)
    return gecenler, gecemeyenler

#------------------------------------------------------
if __name__ == "__main__":
    ogrenciler = []  # Öğrencileri tutacak liste
    
    # Kullanıcıdan öğrenci isimleri ve notlarını alalım
    n = int(input("Kaç öğrenci gireceksiniz? "))  # Öğrenci sayısını al
    for i in range(n):
        isim = input(f"{i+1}. öğrencinin ismini girin: ")
        notu = int(input(f"{isim} öğrencisinin notunu girin: "))
        ogrenciler.append(SinavRaporu(isim, notu))  # Öğrenci nesnesi oluşturulup listeye ekleniyor
    
    # Geçme sınırını alalım
    limit = int(input("Geçme sınırını girin: "))
    
    # Geçen ve geçemeyen öğrencileri bulalım
    gecenler, gecemeyenler = gecti(ogrenciler, limit)
    
    # Sonuçları yazdıralım
    print("\nGeçen Öğrenciler:")
    if gecenler:
        for ogr in gecenler:
            print(ogr)
    else:
        print("Hiçbir öğrenci geçemedi.")
    
    print("\nGeçemeyen Öğrenciler:")
    if gecemeyenler:
        for ogr in gecemeyenler:
            print(ogr)
    else:
        print("Hiçbir öğrenci kalmadı.")

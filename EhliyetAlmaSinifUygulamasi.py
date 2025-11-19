class Ehliyet:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

# Kullanıcıdan kişiler alınır ve ehliyet durumu hesaplanır
def ehliyetSorgusu(sorgulanacakKisiler:list, yasSinir:int):
    hakKazanan = []
    hakKazanmayan = []
    for kisi in sorgulanacakKisiler:
        if kisi.yas >= yasSinir:
            hakKazanan.append(kisi.isim)
        else:
            hakKazanmayan.append(kisi.isim)
    return hakKazanan, hakKazanmayan

# --- Kullanıcı giriş kısmı ---
kisiler = []
kisi_sayisi = int(input("Kaç kişi gireceksiniz?: "))

for _ in range(kisi_sayisi):
    isim = input("Kişinin ismini girin: ")
    yas = int(input("Yaşını girin: "))
    kisiler.append(Ehliyet(isim, yas))

yas_siniri = int(input("Ehliyet yaş sınırını girin: "))

# Sonuçların alınması
hakKazanan, hakKazanmayan = ehliyetSorgusu(kisiler, yas_siniri)

print("\nEhliyet almaya hak kazananlar:")
for isim in hakKazanan:
    print("-", isim)

print("\nEhliyet alamayanlar:")
for isim in hakKazanmayan:
    print("-", isim)

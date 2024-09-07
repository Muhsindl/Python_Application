ürünSayisi = int(input("Ürün sayısı giriniz: "))

# Boş bir liste ile tüm ürünleri depolayacağız
ürünler = []

for i in range(ürünSayisi):
    ürünAdi = input("Ürün adı giriniz: ")
    ürünFiyat = int(input(f"{ürünAdi} Ürün fiyatı giriniz: "))
    
    # Her ürün için bir sözlük oluşturuyoruz
    sozluk = {
        "İsim": ürünAdi,
        "Fiyat": ürünFiyat
    }
    ürünler.append(sozluk)

print("Ürünler listesi:", ürünler)

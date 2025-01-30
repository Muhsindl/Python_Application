# Dönem sayısının kullanıcıdan alınması
donem_Sayisi = int(input("Dönem sayısı giriniz: "))

krediler = []
donem_Ortalamaları = []

# Güz ve Bahar dönemi toplam kredi ve ortalamanın alınması
for i in range(1, donem_Sayisi + 1):
    if i % 2 != 0:
        ortalama = float(input(f"{i}. güz dönemi ortalaması: "))
        kredi = float(input(f"{i}. güz dönemi toplam kredisi: "))
    else:
        ortalama = float(input(f"{i}. bahar dönemi ortalaması: "))
        kredi = float(input(f"{i}. bahar dönemi toplam kredisi: "))
    
    krediler.append(kredi)
    donem_Ortalamaları.append(ortalama)

# Krediler ve dönem ortalamalarını eşleşmiş liste haline getirme
agno = list(zip(krediler, donem_Ortalamaları))

# Toplam krediyi hesaplama
toplam_kredi = sum(kredi for kredi, _ in agno)

# Ağırlıklı ortalamayı hesaplama
agirlikli_ortalama = sum(kredi * ortalama for kredi, ortalama in agno)

# Genel AGNO hesaplama
genel_agno = agirlikli_ortalama / toplam_kredi if toplam_kredi > 0 else 0

print("-"*50)
print(f"Toplam Kredi: {toplam_kredi}, Genel AGNO: {genel_agno:.2f}")
print("-"*50)
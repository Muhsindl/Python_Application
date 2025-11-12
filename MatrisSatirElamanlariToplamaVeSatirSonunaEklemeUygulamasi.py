def row_sums(my_matrix: list):
    for i in range(len(my_matrix)):
        toplam = 0
        for j in range(len(my_matrix[i])):  # Satırdaki her elemanı topla
            toplam += my_matrix[i][j]
        my_matrix[i].append(toplam)  # Satır toplamını ekle

# Kullanıcıdan matris boyutlarını al
satir_sayisi = int(input("Matrisin satır sayısını girin: "))
sutun_sayisi = int(input("Matrisin sütun sayısını girin: "))

# Matrisin elemanlarını kullanıcıdan al
matris = []
for i in range(satir_sayisi):
    satir = []
    for j in range(sutun_sayisi):
        eleman = int(input(f"Matrisin ({i}, {j}) elemanını girin: "))
        satir.append(eleman)
    matris.append(satir)

# Satır toplamlarını ekleyelim
row_sums(matris)

# Sonucu yazdıralım
print("\nSonuç Matris (Satır toplamları eklenmiş hali):")
for satir in matris:
    print(satir)

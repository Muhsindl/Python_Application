#Kullanıcıdan Vize ve Final notu alındı
vize_notu = float(input("Vize notunu girin (0-100 arasında): "))
final_notu = float(input("Final notunu girin (0-100 arasında): "))

# Vize notunun genel not ortalamasına etkisi %40 ve final notunun genel not ortalamasına etkisi %60
ortalama = (vize_notu * 0.4) + (final_notu * 0.6)

#Harf notları koşullandırıldı
if 90 <= ortalama: 
    harf_notu = "AA"
elif 85 <= ortalama:
    harf_notu = "BA"
elif 80 <= ortalama:
    harf_notu = "BB"
elif 75 <= ortalama:
    harf_notu = "CB"
elif 70 <= ortalama:
    harf_notu = "CC"
elif 65 <= ortalama:
    harf_notu = "DC"
elif 60 <= ortalama:
    harf_notu = "DD"
else:
    harf_notu = "FD"

# Geçme durumu kontrol edildi
if harf_notu != "FD":
    durum = "Geçti"
else:
    durum = "Kaldı"

print(f"Ortalama: {ortalama}")
print(f"Harf Notu: {harf_notu}")
print(f"Durum: {durum}")
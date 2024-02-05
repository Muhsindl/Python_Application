"""
(Normalizasyon için dizinin en büyük elemanına bölme işlemi uygulanmıştır)
"""
ozellikAdı=input("Özellik adını giriniz: ")
ozellikDizi=[]
normalizasyonDizisi=[]
ozellikSayısı=int(input("Veri sayısı giriniz: "))
#Veri ekler diziye
for i in range(ozellikSayısı):
    ekle=float(input("Veri değeri giriniz: "))
    ozellikDizi.append(ekle)
#Normalizasyon yapar diziye
for i in range(ozellikSayısı):
    normalizasyonDiziElaman=float(ozellikDizi[i]/max(ozellikDizi))
    normalizasyonDizisi.append(normalizasyonDiziElaman)

print("\n","+"*50)
print("Dizinin Normal hali; ")
print(ozellikDizi)
print("-"*50)        
print("Dizinin Normalizasyon uygulanmış hali; ")
print(normalizasyonDizisi)
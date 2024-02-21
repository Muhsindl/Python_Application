ogrenciNot=[]
toplamNot=0
sınıfMevcut=int(input("Sınıf mevcudu giriniz: "))
#Öğrenci notları alınır ve diziye eklenir
for i in range(sınıfMevcut):
    ogrNot=int(input(f"{i+1}.nci Öğrenci notunu giriniz: "))
    ogrenciNot.append(ogrNot)
    toplamNot=ogrenciNot[i]+toplamNot

#Ortalama hesaplanır
ortalama=toplamNot/sınıfMevcut

#Geçen Öğrenci sayısı belirlenir
gecenOgrenci=0
for i in range(sınıfMevcut):
    if ogrenciNot[i]>ortalama or ogrenciNot[i]>=50:
        gecenOgrenci+=1

print("Geçen öğrenci sayısı: ",gecenOgrenci)
print("Kalan öğrenci sayısı: ",sınıfMevcut-gecenOgrenci)
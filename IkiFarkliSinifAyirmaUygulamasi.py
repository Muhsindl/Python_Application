# Dizimizi tanımlıyoruz
students=["d1","d2","d3","d4","d5","d6","d7","d8","d9","d10"]
# İki farklı boş dizi oluşturuyoruz
A_students=[]
B_students=[]

#Fonksiyonumuzu oluşturuyoruz
def divide_students(students=students):
    for i,s in enumerate(students):
        #Çift ise A dizisine ekliyoruz
        if i%2==0:
            A_students.append(s)
        #Tek ise B dizisine ekliyoruz
        else:
            B_students.append(s)
    #Dizimizi geri döndürüyoruz
    return A_students,B_students

#Fonksiyondan gelen geri dönüşleri alıyoruz
cift,tek=divide_students(students)

#Ekrana yazdırıyoruz
print("Çift Numaralı Öğrenciler: ",A_students)
print("Tek Numaralı Öğrenciler: ",B_students)
# Sınırsız sayıda parametre alan fonksiyon
def func(*x):
    toplam=0
    for i in x:
        toplam=toplam+i
    return toplam
#Girilen sınırsız sayıda parametrenin toplanması 
print(func(1,2,3,4,5))
print(func(1,2))
print(func())
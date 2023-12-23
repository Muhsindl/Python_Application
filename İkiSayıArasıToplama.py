#Kullanıcıdan sayı alma
alt=int(input("Alt limit giriniz: "))
ust=int(input("Üst limit giriniz: "))

toplam=0
for i in range(alt,ust):
    toplam=toplam+i
print(toplam)
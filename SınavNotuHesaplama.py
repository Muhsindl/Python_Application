#Kullanıcıdan doğru ve yanlış sayısı alma
dogru=int (input("Doğru sayınızı giriniz: "))
yanlis=int(input("Yanlış sayınızı giriniz: "))
puan=0

dogrupuan=dogru*10
yanlispuan=yanlis*-5

puan=dogrupuan+yanlispuan
print(puan)
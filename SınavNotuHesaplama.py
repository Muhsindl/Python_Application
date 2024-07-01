#Kullanıcıdan doğru ve yanlış sayısı alma
dogru=int (input("Doğru sayınızı giriniz: "))
yanlis=int(input("Yanlış sayınızı giriniz: "))
puan=0
#Doğru bilinen 10 puan etki etmektedir.
dogrupuan=dogru*10
#Yanlış bilinen sorular -5 puan etki etmektedir.
yanlispuan=yanlis*-5

puan=dogrupuan+yanlispuan
print(puan)
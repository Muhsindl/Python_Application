liste=[]
#Kullanıcıdan liste için veri alma işlemi
for i in range(10):
    n=int(input("Veri gir: "))
    liste.append(n)
#Kullanıcıdan listede aranacak verinin değerini alma
arananSayi=int(input("Listede aranacak veriyi gir: "))

#Kullanıcının girdiği veri varsa veri sayısını ve bulunduğunu bildiren, bulunmuyo ise bulunmadığını bildirir
if arananSayi in liste:
    print("Veri bulunmaktadır")
    print("Bulunan miktar",liste.count(arananSayi))
else:
    print("Girilen veriye ulaşılamadı")

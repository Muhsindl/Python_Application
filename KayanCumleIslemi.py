#Kullanıcıdan cümle alır.
cumle=input("Cümle giriniz: ")
dizi=[]
#Cümleyi diziye atar.
for i in range(len(cumle)):
    dizi.append(cumle[i])
#Adım sayısı kadar dizi elemanlarını kaydırır.
step=int(input("Adım sayısı giriniz:"))
#Dizi elemanlarını kaydırır.
for i in range(step):
    dizi.append(dizi[0])
    del dizi[0]
    print("".join(dizi)) #Dizi elemanlarını birleştirir.
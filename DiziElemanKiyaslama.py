#Dizi eleman sayısını kullanıcıdan al
elemanSayisi=int(input("Eleman sayısı giriniz: "))
dizi=list()
#Dizi elemanlarını kullanıcıdan al
for i in range(elemanSayisi):
    eleman=int(input(f"{i+1}. elemanı giriniz: "))
    dizi.append(eleman)
#Kıyaslanacak sayıyı kullanıcıdan al
x=int(input("Kıyaslanacak sayıyı giriniz: "))

count=0
#Dizi içerisindeki elemanların kaç tanesi girilen sayıdan küçük olduğunu bul
for i in range(elemanSayisi):
    if(x<dizi[i]):
        count+=1
#Sonucu ekrana yazdır
print(f"Girilen \"{x}\" elemanı dizimizde ki \"{count}\" elemandan küçüktür")
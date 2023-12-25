n=int(input("Eleman sayısı giriniz: "))
dizi1=[]
#Elaman girişi
for i in range(n):
    eleman=int(input("Eleman giriniz: "))
    dizi1.append(eleman)

#En çok tekrar eden sayıyı bulma 
enCokTekrar=None
enCokTekrarSayısı=0
for i in dizi1:
    tekrar=dizi1.count(i)
    if tekrar>enCokTekrarSayısı:
        enCokTekrarSayısı=tekrar
        enCokTekrar=i
print("En çok tekrar eden sayı: ",enCokTekrar,"Tekrar miktarı: ",enCokTekrarSayısı)
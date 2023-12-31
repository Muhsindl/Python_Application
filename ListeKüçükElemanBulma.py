dizi=[]
n=int(input("Eleman sayısı giriniz: "))
for i in range(n):
    eleman = int(input(f"{i+1}. elemanı gir: "))
    dizi.append(eleman)
minEleman=dizi[0]
for i in dizi:
    if i<minEleman:
        minEleman=dizi[i]
print("En küçük Eleman:",minEleman)
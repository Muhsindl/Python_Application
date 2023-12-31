dizi=[]
n=int(input("Eleman sayısı giriniz: "))
for i in range(n):
    eleman = int(input(f"{i+1}. elemanı gir: "))
    dizi.append(eleman)
maxEleman=dizi[0]
for i in dizi:
    if i>maxEleman:
        maxEleman=i
print("En büyük Eleman:",maxEleman)
sayi=int(input("sayı giriniz: "))
sayi=str(sayi)
basamak=len(sayi)
cevap=0
for i in range(basamak):
    cevap+=(int(sayi[i])**basamak)
print(f"{sayi} sayısının üstel cevabı: {cevap}")
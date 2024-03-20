sayi=int(input("Decimal tabanda sayı gir:"))
top=0
i=0
#Sayimiz 2 den büyük olana kadar işlem yapılacaktır
while(sayi>=2):
    top=top+((sayi%2)*10**i)
    sayi=sayi//2
    i+=1
top=top+(sayi*(10**i))

print(top)

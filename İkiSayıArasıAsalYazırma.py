nAlt=int(input("Alt limit giriniz: "))
nUst=int(input("Üst limit giriniz: "))
for i in range(nAlt,nUst):
    sayac=0
    for j in range(2,i):
        if i%j==0:
            sayac=1
    if sayac==0:
        print(i)
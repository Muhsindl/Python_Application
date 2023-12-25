altLimit=int(input("Alt limit sayısı gir: "))
ustLimit=int(input("Üst limit sayısı gir: "))
for i in range(altLimit,ustLimit):
    for j in range(1,i):
        if i%j==0:
            toplam=toplam+j
    if toplam>i:
        print("Zengin(Abundant)sayıdır",toplam,">",i)
    toplam=0
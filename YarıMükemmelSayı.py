altSayı=int(input("Alt limit: "))
ustSayı=int(input("Üst limit: "))

for i in range(altSayı,ustSayı):
    sayac=0
    toplam=0
    for j in range(i-1,1,-1):
        if sayac<3:
            if i%j==0:
                toplam=toplam+j
                sayac+=1
    if toplam==i:
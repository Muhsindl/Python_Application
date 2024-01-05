altLimit=int(input("Alt limit giriniz: "))
ustLimit=int(input("Üst limit giriniz: "))
sayac=0
for i in range(altLimit,ustLimit+1):
    for j in range(1,i+1):
        if i%j==0:
            sayac+=1
    if i%sayac==0:
        print(i)
    sayac=0
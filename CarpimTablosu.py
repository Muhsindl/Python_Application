giris=int(input("Alt Sınır giriniz: "))
son=int(input("Üst Sınır giriniz: "))
for i in range(giris,son+1):
    print()
    for j in range(0,11):
        print(i,"x",j,"=",i*j)
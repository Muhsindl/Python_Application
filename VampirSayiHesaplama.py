sayi=input("Sayı giriniz: ")
ilk=sayi[1::-1]
son=sayi[2:4]

if int(sayi)==int(ilk)*int(son):
    print("Vampire sayıdır")
else:
    print("Vampir sayı değildir")
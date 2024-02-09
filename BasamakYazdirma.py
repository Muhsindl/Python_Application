sayi=input("Sayı giriniz: ")
if int(sayi)<0:
    print("Negatif")

for i in range(len(sayi)):
    if i==0:
        print("Birler Basamağı: ",sayi[i])
    elif i==1:
        print("Onlar Basamağı: ",sayi[i])
    elif i==2:
        print("Yüzler Basamağı: ",sayi[i])
    elif i==3:
        print("Binler Basamağı: ",sayi[i])
    elif i==4:
        print("On Binler Basamağı: ",sayi[i])
    elif i==5:
        print("Yüz Binler Basamağı: ",sayi[i])
    elif i==6:
        print("Milyonlar Basamağı: ",sayi[i])
    elif i==7:
        print("On Milyonlar Basamağı: ",sayi[i])
    elif i==8:
        print("Yüz Milyonlar Basamağı: ",sayi[i])
    else:
        print("Geçersiz sayı")
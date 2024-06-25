sifre=[]
#Kelime sayısı alınıyor kullanıcıdan
boyut=int(input("Harf sayısı giriniz: "))
#Her kelime dizide eleman olarak bulunuyor

for i in range(boyut):
    eleman=int(input("Şifre giriniz: "))
    sifre.append(eleman)

#6 33 777 44 2 22 2 ==> MERHABA   
sonuc="Şifreniz: "
for i in sifre:
    if i==2:
        sonuc+="a"
    elif i==22:
        sonuc+="b"
    elif i==222:
        sonuc+="c"
    elif i==3:
        sonuc+="d"
    elif i==33:
        sonuc+="e"
    elif i==333:
        sonuc+="f"
    elif i==4:
        sonuc+="g"
    elif i==44:
        sonuc+="h"
    elif i==444:
        sonuc+="ı"
    elif i==5:
        sonuc+="j"
    elif i==55:
        sonuc+="k"
    elif i==555:
        sonuc+="l"
    elif i==6:
        sonuc+="m"
    elif i==66:
        sonuc+="n"
    elif i==666:
        sonuc+="o"
    elif i==7:
        sonuc+="p"
    elif i==77:
        sonuc+="q"
    elif i==777:
        sonuc+="r"
    elif i==7777:
        sonuc+="s"
    elif i==8:
        sonuc+="t"
    elif i==88:
        sonuc+="u"
    elif i==888:
        sonuc+="v"
    elif i==9:
        sonuc+="w"
    elif i==99:
        sonuc+="x"  
    elif i==999:
        sonuc+="y"
    elif i==9999:
        sonuc+="z"

print("Mesaj Sonucu:\n",sonuc)
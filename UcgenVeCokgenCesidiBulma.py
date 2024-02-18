kenarSayisi=int(input("Kenar sayısı giriniz: "))
kenarDizi=[]
sayac=0
if kenarSayisi>3:
    for i in range(kenarSayisi):
        eleman=int(input(f"{i+1}. kenarı giriniz: "))
        kenarDizi.append(eleman)
    for j in (kenarDizi):
        if j==kenarDizi[i]:
            sayac+=1
    if sayac==4:
        print("Kare")
    else:
        print("Çokgen")
else:
    for i in range(kenarSayisi):
        eleman=int(input(f"{i+1}. kenarı giriniz: "))
        kenarDizi.append(eleman)
        
    if kenarDizi[0]==kenarDizi[1] and kenarDizi[0]==kenarDizi[2]:
        print("Eş Kenar Üçgen")
    elif kenarDizi[0]==kenarDizi[1] or kenarDizi[0]==kenarDizi[2]:
        print("İkiz Kenar Üçgen")
    else:
        print("Çeşit Kenar Üçgen")
def rakamTopla(sayi):
    toplam=0
    for each in sayi:
        toplam+=int(each)
    print("Rakamlarının toplamı: ",toplam)

ksayı=input("Rakamları toplanacak sayıyı giriniz: ")
rakamTopla(ksayı)
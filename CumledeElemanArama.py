# Kullanıcıdan metin alınır ve bu metin içerisinde aranacak karakter girilir.
text=input("Cümle giriniz: ")
ara=input("Aranacak karakteri giriniz:")
# Eğer aranacak karakter 1 karakterden fazla ise hata mesajı verilir.
if len(ara)<=1:
    sayac=0
    # Metin içerisinde aranacak karakterin kaç adet olduğunu bulmak için döngü oluşturulur.
    for i in text:
        # Eğer aranacak karakter metin içerisinde var ise sayac değişkeni 1 arttırılır.
        if ara==i:
            sayac+=1

    print(f"{text} cümlesin de bulunan {ara} karakteri sayısı {sayac} kadardır.")
else:
    print("HATA!! Yalnız bir adet aranacak eleman giriniz")
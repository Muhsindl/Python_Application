# Fonksiyon: Encryption
def Encryption(sayi1,sayi2):
    return sayi1%sayi2
# Kullanıcıdan alınan değerlerle fonksiyonu çağırıp sonucu ekrana yazdırma
boyut=int(input("Şifre alan boyutu giriniz:"))
sifreleme=int(input("Şifrelenecek Sayı giriniz: "))
# Fonksiyonu çağırma
encrypt=Encryption(sifreleme, boyut)
# Sonucu ekrana yazdırma
print("Şifrelenmiş hali: {}".format(encrypt))
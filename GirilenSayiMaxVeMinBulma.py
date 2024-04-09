#Kullanıcıdan sayı alınır
sayi=(input("Sayı giriniz: "))
#Varsayılan olarak max ve min değerler 0 ve 1 olarak belirlenir
maxim=0
minim=1
#Sayı içindeki her bir elemanı kontrol eder ve max ve min değerlerini bulur
for i in sayi:
    if int(i)>int(maxim):
        maxim=i
    if int(i)<int(minim):
        minim=i
#Max ve min değerleri ekrana yazdırır
print(f"Maximum Değer: {maxim} minimum değer {minim}")
# ASCII Code

# Kullanıcıdan karakter alınması
karakter = input("Karakter giriniz lütfen: ")

# Tek basamaklı karakter mi ve sözel bir ifade mi diye kontrol ediliyor
if len(karakter) == 1 and karakter.isalpha(): 
    print(f"Karaktere ({karakter}) ait ASCII kodu => {ord(karakter)}")
else:
    print("String(harf) formatında ve tek karakter girişi yapın lütfen")
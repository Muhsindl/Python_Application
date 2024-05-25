#Kullanıcıdan dizi boyutu alınıyor.
boyut = int(input("Dizi boyutu giriniz: "))
dizi = []
#Dizi elemanları kullanıcıdan alınıyor.
for i in range(boyut):
    eleman = int(input(f"{i+1}. Elemanı giriniz: "))
    dizi.append(eleman)

tekrar_sayilari = {}
#Dizideki elemanların tekrar sayıları hesaplanıyor.
for eleman in dizi:
    if eleman in tekrar_sayilari:
        tekrar_sayilari[eleman] += 1
    else:
        tekrar_sayilari[eleman] = 1
#Dizideki elemanların tekrar sayıları ekrana yazdırılıyor.
for eleman, sayac in tekrar_sayilari.items():
    print(f"Dizide bulunan {eleman} sayısından {sayac} adet bulunuyor.")
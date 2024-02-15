dizi=[]
ciftToplam=0
tekToplam=0
girilecekSayi=int(input("Girilecek sayı miktarı: "))
for i in range(girilecekSayi):
    eleman=int(input(f"{i+1}. Sayıyı giriniz: "))
    dizi.append(eleman)
    if dizi[i]%2==0:
        ciftToplam+=dizi[i]
    else:
        tekToplam+=dizi[i]

print("tek sayıların çiftsayılara oranı: ",f"{tekToplam}/{ciftToplam}",tekToplam/ciftToplam)
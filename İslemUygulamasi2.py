# Kullanıcıdan alınan sınır değeri kadar serinin toplamını hesaplayan program
sinir=int(input("Sınır giriniz: "))
toplam=0
sayac=0
# 1-1/3+1/5-1/7 ... hesaplamasının yapıldığı kısım
for i in range((2*sinir)+1):
    # i değeri tek ise
    if i%2!=0:
        # sayac değeri çift ise
        if sayac%2==0:
            toplam=toplam+(1/i)
        # sayac değeri tek ise
        else:
            toplam=toplam-(1/i)
        sayac+=1            
# Sonuç ekrana yazdırılır
print("Sonuç: ",toplam)




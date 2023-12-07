n=int(input("Sayı giriniz: "))
#Toplama için etkisiz eleman atanır
toplam=0
#Çarpma için etkisiz eleman atanır
carpim=1
#Döngümüz ile işlem yapılır
for i in range(n+1):
    if i%2==1:
        toplam=toplam+i
        carpim=carpim*i

print("Toplam: ",toplam,"\nÇarpım: ",carpim)
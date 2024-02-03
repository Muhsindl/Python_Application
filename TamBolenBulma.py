#Sayı alınması
n=int(input("Sayı gir:"))
#Sayac tanımı bölen sayısının yazdırılmasında kullanılacak
sayac=0

for i in range(1,n+1):
    if(n%i==0):
        sayac+=1
        print("{}. Bölen:".format(sayac),i)

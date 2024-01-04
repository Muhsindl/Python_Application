n=int(input("Sayı giriniz: "))
sayac=0

for i in range(1,n+1):
    if n%i==0:
        sayac=sayac+1
if n%sayac==0:
    print("TAU sayısıdır.")
else:
    print("TAU sayısı değildir")
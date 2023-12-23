alt=int(input("Alt limit giriniz: "))
ust=int(input("Üst limit giriniz: "))
ckare=0
tkup=0
for i in range(alt,ust):
    if i%2==0:
        ckare+=i**2
    else:
        tkup+=i**3
print("Çift sayılar karesi: ",ckare)
print("Tek sayılar küp: ",tkup)
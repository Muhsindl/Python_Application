n=int(input("Sphere kaça kadar hesaplanacak: "))
toplam=0
for i in range(n+1):
    toplam=toplam+i**2
    print(i,"nci adım için: ",toplam)
n=int(input("Sayı gir: "))
n=str(n)
toplam=0
for i in n:
    toplam=toplam+int(i)
if int(n)%toplam==0:
    print("Harshad Sayıdır")    
else:
    print("Harshad sayı değildir")
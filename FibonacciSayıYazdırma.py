n=int(input("Basamak sayısı giriniz: "))
n1=1
n2=1
n3=n1+n2
print("1-1",end="-")
for i in range(n-2):
    print(n3,end="-")
    n1=n2
    n2=n3
    n3=n1+n2
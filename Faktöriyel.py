n=int(input("Sayı giriniz: "))
def fact(n):
    carp=1
    for i in range(1,n+1):
        carp=carp*i
    return carp

print(fact(n))
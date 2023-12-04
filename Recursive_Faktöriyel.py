n=int(input("Sayı giriniz: "))
def fakt(n):
    if n<=1:
        return 1
    else:
        return n*fakt(n-1)
print(fakt(n))
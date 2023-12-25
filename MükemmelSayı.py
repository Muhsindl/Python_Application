n1=int(input("Alt Limit Sayı giriniz: "))
n2=int(input("Üst Limit Sayı giriniz: "))

toplam=0
for i in range(n1,n2):
    for j in range(1,i):
        if i%j==0:
            toplam+=j
    if toplam==i:
        print("Mükemmel Sayı: ",i,"\n")
    toplam=0
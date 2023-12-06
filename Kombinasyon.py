#Kullanıcıdan n ve r değerleri alınması
n=int(input("N değeri giriniz: "))
r=int(input("R değeri giriniz: "))

x=n-r
nfakt=1
xfakt=1
rfakt=1
# n!
for i in range(1,n+1):
    nfakt =i*nfakt
#(n-r)! işlemi
for i in range(1,r+1):
    xfakt =i*xfakt
#r! işlemi
for i in range(1,x+1):
    rfakt =i*rfakt

# n!/(n-r!)*r! işleminin yapılması
kombinasyon=nfakt/(xfakt*rfakt)
print(kombinasyon)
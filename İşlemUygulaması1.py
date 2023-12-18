# ∑i=0 5*i+6 denklemi çözümü

# Kullanıcıdan son girdi alma
n=int(input("Bir n değeri giriniz: "))

toplam=0
#İşlem yapılması
for i in range(0,n+1):
    toplam=5*i+6+toplam
print(toplam)
# ax2+ bx +c = 0 fonksiyonunun diskriminantını hesaplayan program
a=int(input("A değeri giriniz: "))
b=int(input("B değeri giriniz: "))
c=int(input("C değeri giriniz: "))
# Δ = b2 - 4ac
diskriminant=(b**2)-(4*a*c)
# Ekrana yazdırma
print(f"Diskriminant (Δ):{diskriminant}")
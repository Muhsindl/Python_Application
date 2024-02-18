ilkHız=int(input("İlk Hız giriniz: "))
zaman=int(input("Zaman giriniz: "))
ivme=int(input("İvme giriniz: "))

hız=ilkHız+(ivme*zaman)
yol=(ilkHız*zaman)+(((1/2)*ivme)*(zaman**2))

print(f"Yol:{yol}")
print(f"Hız:{hız}")
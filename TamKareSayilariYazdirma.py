altSinir=int(input("Alt sınır giriniz: "))
üstSinir=int(input("Üst sınır giriniz: "))
print("-"*50)
for i in range(üstSinir+1):
    if altSinir<i**2<üstSinir:
        print(f"Sayı: {i} karesi ise {i**2}")
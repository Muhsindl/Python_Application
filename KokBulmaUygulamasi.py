import math  
import cmath  # Karmaşık sayılar için

# İkinci derece denklemin köklerini hesaplayan program
# Denklem: ax^2 + bx + c = 0 

# Kullanıcıdan a, b, c değerlerini al
a = int(input("a değerini giriniz: "))
b = int(input("b değerini giriniz: "))
c = int(input("c değerini giriniz: "))

# a = 0 durumunu kontrol et (ikinci derece denklem olmalı)
if a == 0:
    print("Hata: 'a' değeri 0 olamaz, ikinci derece denklem için a ≠ 0 olmalıdır.")
else:
    # Diskriminantı hesapla
    discriminant = (b**2) - (4*a*c)

    # Gerçek kökler
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Gerçek kökler:")
        print(f"Kök 1: {root1}")
        print(f"Kök 2: {root2}")

    # Çift katlı kök (Aynı iki kök)
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"Çift katlı kök: {root}")

    # Karmaşık kökler 
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print(f"Karmaşık kökler:")
        print(f"Kök 1: {root1}")
        print(f"Kök 2: {root2}")

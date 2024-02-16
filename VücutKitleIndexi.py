agirlik=int(input("Ağırlık giriniz (kilogram): "))
boy=float(input("Boy giriniz (metre): "))
vki=agirlik/(boy**2)
if vki<18.5:
    print("İdeal kilonun altında")
elif vki<24.9:
    print("İdeal kiloda")
elif vki<29.9:
    print("İdeal kilonun üstünde")
elif vki<39.9:
    print("İdeal kilonun çok üstünde (obez)")
else:
    print("İdeal kilonun çok üstünde (morbid obez)")
print(vki)
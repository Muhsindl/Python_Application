a=int(input("Birinci Kenar: "))
b=int(input("İkinci Kenar: "))
c=int(input("Üçüncü Kenar: "))
#Eşkenar üçgen
if a==b & a==c:
    print("Eşkenar üçgen")
#İkizkenar üçgen
elif a==b | a==c:
    print("İkizkenar üçgen")
#Çeşitkenar üçgen
else:
    print("Çeşitkenar üçgen")
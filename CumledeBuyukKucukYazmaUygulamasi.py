#Kullanıcıdan cümle alınması
text=input("Cümle giriniz: ")

for each in range(len(text)):
    #Çift indisleri büyük yazar
    if each%2==0:
        print(text[each].upper(),end="")
    #Tek indisleri küçük yazar
    else:
        print(text[each].lower(),end="")
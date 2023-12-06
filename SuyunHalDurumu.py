#Kullanıcıdan Suyun Sıcaklık(Celcius) derecesinin alınması
n=int(input("Sıcaklık gir: "))
if n>=100:
    print("Gaz halinde")
elif 0<n<100:
    print("Sıvı halinde")
else:
    print("Katı halinde")
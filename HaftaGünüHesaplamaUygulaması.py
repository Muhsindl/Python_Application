n=int(input("Sayı giriniz: "))

if (0<n<=7):
    if n==1:
        print("Pazartesi")
    elif n==2:
        print("Salı")
    elif n==3:
        print("Çarşamba")
    elif n==4:
        print("Perşembe")
    elif n==5:
        print("Cuma")
    elif n==6:
        print("Cumartesi")
    else:
        print("Pazar")
else:
    print("Lütfen 1-7 arasında sayı giriniz")
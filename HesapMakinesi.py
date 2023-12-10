class Calculator:
    # init metodu
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        result = self.n1 + self.n2
        return result

    def multiplication(self):
        result = self.n1 * self.n2
        return result
    def division(self):
        result = self.n1 / self.n2
        return result
    def subtraction(self):
        result = self.n1 - self.n2
        return result

print("Toplama için (1), çarpma işlemi için (2), bölme işlemi için (3), çıkarma işlemi için (4) seçiniz.")
select = input("1,2,3 ya da 4 giriniz: \n")
s1 = int(input("Birinci sayı: "))
s2 = int(input("İkinci sayı: "))
c1 = Calculator(s1, s2)

if select == "1":
    print("Toplama {}".format(c1.add()))
elif select == "2":
    print("Çarpma {}".format(c1.multiplication()))
elif select == "3":
    print("Bölme {}".format(c1.division()))
elif select == "4":
    print("Çıkarma {}".format(c1.subtraction()))
else:
    print("Hata belirtilen sayılar dışında seçim yapıldı")
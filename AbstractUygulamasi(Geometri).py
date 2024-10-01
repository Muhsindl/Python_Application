from abc import ABC, abstractmethod
# Miras alınacak (Inheritance) yapılacak bir sınıf oluşturuldu
class Shape(ABC):
    def _init_(self):
        pass
    # "calculate_area" fonksiyonu soyut(abstract) olarak oluşturuldu ve kullanılmak zorunda bırakıldı
    @abstractmethod
    def calculate_area(self):
        pass
    # "calculate_perimeter" fonksiyonu soyut(abstract) olarak oluşturuldu ve kullanılmak zorunda bırakıldı
    @abstractmethod
    def calculate_perimeter(self):
        pass
# Çember için sınıf oluşturuldu 
class Circle(Shape):
    def _init_(self,r,pi=3.14):
        self.r=r
        self.pi=pi
    def calculate_area(self):
        return self.pi*(self.r**2)
    def calculate_perimeter(self):
        return 2*self.pi*self.r
# Dikdörtgen için sınıf oluşturuldu
class Rectangle(Shape):
    def _init_(self,kenar1,kenar2):
        self.kenar1=kenar1
        self.kenar2=kenar2
    def calculate_area(self):
        return self.kenar1*self.kenar2
    def calculate_perimeter(self):
        return 2*(self.kenar1+self.kenar2)
# Üçgen için sınıf oluşturuldu
class Triangle(Shape):
    def _init_(self,h,taban,kenar1=1,kenar2=1,kenar3=1):
        self.kenar1=kenar1
        self.kenar2=kenar2
        self.kenar3=kenar3
        self.taban=taban
        self.h=h
    def calculate_area(self):
        return (self.taban*self.h)/2
    def calculate_perimeter(self):
        return (self.kenar1+self.kenar2+self.kenar3)

# Oluşturuldan sınıflardan nesne oluşturuldu alan ve çevre hesaplama işlemi gerçekleştirildi
c1=Circle(15,3)
print("-"*25)
print("Alan: ",c1.calculate_area())
print("Çevre: ",c1.calculate_perimeter())
r1=Rectangle(10,22)
print("-"*25)
print("Alan: ",r1.calculate_area())
print("Çevre: ",r1.calculate_perimeter())
t1=Triangle(10, 5, kenar1=15,kenar2=20,kenar3=25)
print("-"*25)
print("Alan: ",t1.calculate_area())
print("Çevre: ",t1.calculate_perimeter())
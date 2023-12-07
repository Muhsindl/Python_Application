from abc import ABC, abstractmethod

class Sekiller(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def alan(self):
        pass

    def toString(self):
        print("Şekiller")

class Kare(Sekiller):
    def __init__(self,kenar):
        self.kenar=kenar

    def alan(self):
        return self.kenar**2
        

    def toString(self):
        print("Kare")

class Daire(Sekiller):
    pi = 3.14
    def __init__(self,yaricap):
        self.yaricap=yaricap

    def alan(self):
        return self.pi * self.yaricap**2

    def toString(self):
        print("Daire")
                
d1=Daire(4)
k1=Kare(5)
print(k1.alan())
print(d1.alan())
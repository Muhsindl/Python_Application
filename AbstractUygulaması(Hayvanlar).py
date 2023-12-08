from abc import ABC, abstractclassmethod

class HayvanSesi(ABC):
    def __init__(self):
        pass
    @abstractclassmethod #Zorunlu metot
    def kediSes(self):
        print("Miyav..")
    @abstractclassmethod #Zorunlu metot
    def kopekSes(self):
        print("Hav..")   

class Kopek(HayvanSesi):
    def __init__(self):
        pass        
    def kediSes(self):
        print("Miyav..")
    def kopekSes(self):
        print("Hav..")   

class Kedi(HayvanSesi):
    def __init__(self):
        pass    
    def kediSes(self):
        print("Miyav..")
    def kopekSes(self):
        print("Hav..")
        
#Nesne oluşturuldu
kopek1=Kopek()
kedi1=Kedi()

#Fonksiyon kullanıldı
kopek1.kopekSes()
kopek1.kediSes()
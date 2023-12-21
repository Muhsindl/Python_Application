from abc import ABC, abstractmethod

class HayvanatBahcesi(ABC):
    @abstractmethod
    def HayvanCinsi(self):
        pass
    
    def HayvanKafesi(self):
        pass

class Papagan(HayvanatBahcesi):
    def __init__(self, ad, tur, kanatBoyu):
        self.ad = ad
        self.tur = tur
        self.kanatBoyu = kanatBoyu
    
    def HayvanCinsi(self):
        return self.tur
    
    def HayvanKafesi(self):
        print("1900 nolu kafes")

class Aslan(HayvanatBahcesi):
    def __init__(self, ad, tur, penceGucu):
        self.ad = ad
        self.tur = tur
        self.penceGucu = penceGucu
    
    def HayvanCinsi(self):
        return self.tur
    
    def HayvanKafesi(self):
        print("1905 nolu kafes")

class Fil(HayvanatBahcesi):
    def __init__(self, ad, tur, hortumBuyuklugu):
        self.ad = ad
        self.tur = tur
        self.hortumBuyuklugu = hortumBuyuklugu
    
    def HayvanCinsi(self):
        return self.tur
    
    def HayvanKafesi(self):
        print("1910 nolu kafes")

p1 = Papagan("Papağan Merry", "Kuş", 5)  
a1 = Aslan("Aslan George", "Kedigil", 3)     
f1 = Fil("Fil John", "Memeli", 8)
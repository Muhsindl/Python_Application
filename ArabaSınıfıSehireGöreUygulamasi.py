class Araba(object):
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model
    def ekranYazdirma(self):
        print(f"Markası:{self.marka}\n Model:{self.model}")

#Kırıkkale sınıfı miras (inheritance) ablınmıştır Araba sınıfından
class KırıkkaleAraba(Araba):
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model

#Ankara sınıfı miras (inheritance) ablınmıştır Araba sınıfından
class AnkaraAraba(Araba):
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model

# Farklı şehirde bulunan araba markaları ve modelleri nesneleri
k1=KırıkkaleAraba("Mercedes",2020)
a1=AnkaraAraba("Audi",2021)

#Ekrana yazdırmak için
k1.ekranYazdirma()
a1.ekranYazdirma()
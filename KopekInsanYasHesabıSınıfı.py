class Kopek():
    yilCarpani=7
    def __init__(self,yas=0):
        self.yas=yas        
    def insanYasiHesapla(self):
        return self.yas*self.yilCarpani

n=int(input("Köpek yaşı: "))
k1=Kopek(n)

print("Hayvan yaşı: {} \nİnsan yaş hesabı: {}".format(n,k1.insanYasiHesapla()))
class Araba(object):
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.hiz = 0

    def hizGosterge(self):
        print("Araç hızı: {}".format(self.hiz))

    def hizlan(self, artis):
        self.hiz += artis
        print("Araç Hızı: {}".format(self.hiz))

    def yavasla(self, azalis):
        self.hiz -= azalis
        print("Araç Hızı: {}".format(self.hiz))

# Araba nesneleri oluşturuldu
a1 = Araba("Ford", "Focus")
a2 = Araba("Mercedes", "C-180")
a3 = Araba("Audi", "A3")

#Sınıf metotları kullanıldı
a1.hizlan(100)
a2.hizlan(120)
a3.hizlan(115)
a1.hizGosterge()
a2.hizGosterge()
a3.hizGosterge()
class Hayvanlar(object):
    def __init__(self):
        print("Hayvalar sınıfı oluşturuldu")

    def toString(self):
        print("hayvanlar")

    def yurumeOzelligi():
        print("Yürüyebilir")

    def ucabilmeOzelligi():
        print("Uçabilir")

    def yuzebilmeOzelligi():
        print("Yüzebilir")


class Omurgalı_Hayvanlar(Hayvanlar):
    def __init__(self):
        super().__init__()
        print("Omurgalı Hayvanlar sınıfı oluşturuldu")

    def toString(self):
        print("Omurgalı Hayvanlar")

    def iskeletSistemi(self):
        print("Kemik yapı")

    def dolasimSistemi(self):
        print("Kapalı dolaşım")


class Omurgasız_Hayvanlar(Hayvanlar):
    def __init__(self):
        super().__init__()
        print("Omurgasız Hayvanlar sınıfı oluşturuldu")

    def toString(self):
        print("Omurgasız Hayvanlar")

    def iskeletSistemi(self):
        print("Kabuklu yapı")

    def dolasimSistemi(self):
        print("Açık dolaşım")


# Nesne oluşturuldu          
p1 = Omurgalı_Hayvanlar()
q1 = Omurgasız_Hayvanlar()
print("-" * 25)

# Sorgulama yapılıyor
p1.toString()
q1.iskeletSistemi()
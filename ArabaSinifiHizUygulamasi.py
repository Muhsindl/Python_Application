class Araba:
    def __init__(self, model, hiz):
        self.model = model
        self.hiz = hiz

# En hızlı arabayı bul
def enHizli(arabalar: list):
    en_hizli = arabalar[0]
    for a in arabalar:
        if a.hiz > en_hizli.hiz:
            en_hizli = a
    return en_hizli

if __name__ == "__main__":
    arabalar = []
    
    while True:
        model = input("Araba modeli: ")
        hiz = int(input("Hızı: "))
        arabalar.append(Araba(model, hiz))  # listeye ekle

        devam = input("Başka araba eklemek ister misiniz? (e/h): ")
        if devam.lower() != "e":
            break

    en_hizli_araba = enHizli(arabalar)
    print("En hızlı araba:", en_hizli_araba.model, "-", en_hizli_araba.hiz, "km/h")

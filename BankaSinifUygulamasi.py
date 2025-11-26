class BankaHesap:
    def __init__(self, iban="TR0000", isim="Boş İsim", bakiye=0):
        self.__iban = iban
        self.isim = isim
        self.__bakiye = bakiye
    
    @property
    def iban(self):
        return self.__iban

    @iban.setter
    def iban(self, iban):
        self.__iban = iban

    @property
    def bakiye(self):
        return self.__bakiye

    @bakiye.setter
    def bakiye(self, bakiye):
        self.__bakiye = bakiye

    def paraYatir(self, para):
        if para > 0:
            self.__bakiye += para
        else:
            return "Negatif para yatırılmaz."
    
    def paraCek(self, para):
        if para <= self.__bakiye and para >= 0:
            self.__bakiye -= para
        else:
            return "Yetersiz bakiye ya da geçersiz tutar!"
    
    def bilgiGoster(self):
        print(f"{self.__iban} IBAN numaralı hesabın sahibi {self.isim} bakiye: {self.__bakiye} TL.")

def main():
    iban = input("Hesap IBAN'ını giriniz: ")
    isim = input("Hesap sahibinin ismini giriniz: ")
    bakiye = int(input("Başlangıç bakiyesi giriniz: "))
    
    # Hesap nesnesi oluşturuluyor
    hesap = BankaHesap(iban, isim, bakiye)
    
    # İşlem seçimi
    karar = int(input("Para çekmek (1) / Para yatırmak (0): "))
    
    if karar == 1:
        para = int(input("Çekilecek tutarı giriniz: "))
        hesap.paraCek(para)
        hesap.bilgiGoster()
    elif karar == 0:
        para = int(input("Yatırılacak tutarı giriniz: "))
        hesap.paraYatir(para)
        hesap.bilgiGoster()
    else:
        print("Geçersiz işlem!")
        hesap.bilgiGoster()

if __name__ == "__main__":
    main()

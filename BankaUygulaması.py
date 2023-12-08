class Banka(object):
    def __init__(self,iban,ucret):
        self.iban=iban
        self.__ucret=ucret
    def getIban(self):
        return self.iban
    def getUcret(self):
        return self.__ucret
    def paraGonder(self,gonder):
        self.__ucret=self.__ucret+gonder
        return self.__ucret
    def paraCek(self,gonder):
        if gonder>self.__ucret:
            print("Yetersiz bakiye")
        else:
            self.__ucret=self.__ucret-gonder
            return self.__ucret

#Nesne oluşturuldu
b1=Banka("710668", 10000)

#Yetersiz bakiye uyarısı 
b1.paraCek(10250)
b1.getUcret()

#Para çekimi yapacaktır
b1.paraCek(10000)
b1.getUcret()

#Para gönderilecektir
b1.paraGonder(10500)
b1.getUcret()
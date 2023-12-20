class Karakter(object):
    def __init__(self,isim,saglıkPuan,saldırıGücü,savunmaGücü):
        self.isim=isim
        self.saglıkPuan=saglıkPuan
        self.saldırıGücü=saldırıGücü
        self.savunmaGücü=savunmaGücü
    def saldırmaGucuArttır(self):
        saldırıGücü=self.saldırıGücü+10
        return saldırıGücü
    def savunmaGucuArttır(self):
        savunmaGücü=self.savunmaGücü+10
        return savunmaGücü
    def karakterTürü(self):
        pass
    
class Hırsız(Karakter):
    __karakterTur="Hırsız"
    def karakterTürü(self):
        return self.__karakterTur
    
class Savascı(Karakter):
    __karakterTur="Savaşçı"
    def karakterTürü(self):
        return self.__karakterTur

class Büyücü(Karakter):
    __karakterTur="Büyücü"
    def karakterTürü(self):
        return self.__karakterTur


h1=Hırsız("Hırsız Nuri", 60, 30, 45)
s1=Savascı("Savaşçı Hakan", 70, 75, 65)
b1=Büyücü("Büyücü Arif", 40, 30, 45)
class Urun(object):
    def __init__(self,oran,ekle,fiyat):
        self.oran=oran
        self.ekle=ekle
        self.fiyat=fiyat
        
    def zamYap(self,oran):
        self.fiyat=self.fiyat+((self.fiyat*oran)/100)   
        return self.fiyat
    
    def stokEkle(self):        
        return self.ekle
    
    def getBilgi(self):
        print("Ürün Fiyatı: ",self.fiyat)
        print("Ürün stok miktarı: ",self.ekle)

#Kullanıcıdan girdi alınır
input_fiyat=int(input("Ürün fiyatı giriniz: "))
input_oran=int(input("Zam oran giriniz: "))
input_ekle=int(input("Stok eklenecek sayı giriniz: "))

#Nesne oluşturulur ve metodlar çağrılır
u1=Urun(input_oran,input_ekle,input_fiyat)
u1.zamYap(input_oran)
u1.getBilgi()
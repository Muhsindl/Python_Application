class Siparis(object):
    #Initilazing metot
    def __init__(self,siparisNo,siparisFiyatı,stok,numara,siparisSayısı):
        self.__siparisNo=siparisNo
        self.siparisSayısı=siparisSayısı
        self.siparisFiyatı=siparisFiyatı
        self.stok=stok      
        self.numara=numara
        #Sınıf metodu
    def siparisHesapla(self):
        if self.siparisSayısı<= self.stok:
            if self.numara==self.__siparisNo:
                self.stok=self.stok-self.siparisSayısı
                ucret=self.siparisFiyatı*self.siparisSayısı
                print(ucret)
            else:
                print("Ürün stokta bulunamadı")
        else:
            print("Stokta o kadar ürün yok")

#Kullanıcıdan eklenecek ürün girdileri alındı
n=input("Eklenecek ürün Id giriniz: ")
fiyat=int(input("Ürün Fiyatı giriniz:"))
stokmiktarı=int(input("Stok Miktarı giriniz:"))

#Kullanıcıdan alınacak ürün girdileri alındı
num=input("Alınacak ürün Id giriniz:")
sayi=int(input("Alınacak Miktar giriniz:"))

s1=Siparis(n,fiyat,stokmiktarı,num,sayi)
s1.siparisHesapla()
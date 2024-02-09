class kitap(object):
    def __init__(self,Id,kitapAdı,kitapBasımYılı,yazar):
        self.Id=Id
        self.kitapAdı=kitapAdı
        self.kitapBasımYılı=kitapBasımYılı
        self.yazar=yazar
        self.mevcut="Mevcut"    
        
    def oduncAl(self,IdNo):
        if self.mevcut=="Mevcut":
            if IdNo==self.Id:
                print(self.kitapAdı,"isimli kitap ödünç verildi.")
                self.mevcut="Mevcut değil"
            else:
                print("Kitap bulunamadı")
        else:
            print("Kitap mevcut değil")
            self.mevcut="Mevcut değil"
            
        
#Kitaplar ekleniyor
k1=kitap(6,"Algoritma Soruları C++",2021,"John Doe")
k2=kitap(7,"Algoritma Soruları Python",2022,"el-Hârizmî")
k3=kitap(71,"Algoritma Soruları Java",2019,"Albert Camus")

#Kitap Ödünç alınıyor
k1.oduncAl(6)
k2.oduncAl(7)
k3.oduncAl(71)

#Alınan bir kitap tekrar alınmaya çalışıldı
k1.oduncAl(6)
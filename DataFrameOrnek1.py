import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sayi=int(input("Sınıf mevcudu giriniz: "))
#Rastgele 0,100 arasında kullanıcının istediği sayıda not oluşturulur
veri=np.random.randint(0,100,sayi)
indis=np.arange(1,sayi+1)
dtf=pd.DataFrame(data=veri,index=indis)

#Sütun'a isim verilir
dtf.columns=["Notlar"]

#50 den yüksek ve ortalamadan yüksek olan notlara Kaldı ve Geçti ifadesi konulur yeni Features(Öz nitelikte)
dtf["Geçme Durumu"]=["Geçti" if (int(i)>dtf["Notlar"].mean() or int(i)>=50)  else "Kaldı" for i in dtf["Notlar"]]

#Boş figur oluşturuldu
plt.figure(figsize=(6,8))
plt.hist(veri,bins=25,alpha=0.45,color="blueviolet")
plt.show()
# Görseli kayıt etmek için
# plt.savefig("kayit.png",dpi=300)
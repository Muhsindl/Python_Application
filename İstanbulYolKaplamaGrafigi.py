import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Verisetini okuduk
dtf=pd.read_csv("C:/Users/Muhsin/Desktop/UKOME Yol Baz_nda (Kesiksiz) Ana Arterler.csv")

#Sütun isimlerini öğreniyoruz
print(dtf.columns)

#Sayısal değerler hakkında bilgi ediniyoruz
print(dtf.describe())

#_id sütununu index yapıyoruz
dtf=dtf.set_index('_id')

#Sütunlara silme işlemi uyguluyoruz
dtf=dtf.drop(columns=["OBJECTID","IBB_KIMLIKNO",'ACIKLAMA', 'UKOME_OZET', 'UKOME_GIRIS','UKOME_CIKIS', 'ANAARTER_TIP', 'SHAPE_Length_1'])
dtf["KAPLAMA_CINSI"]=dtf["KAPLAMA_CINSI"].fillna("Boş veri")

#Boş ve alakasız verileri tablodan sildik
dtf=dtf.drop(dtf[dtf["KAPLAMA_CINSI"]== "Boş veri"].index)
dtf=dtf.drop(dtf[dtf["KAPLAMA_CINSI"]== "1"].index)

#Verisetinde yer alan kaplama cinsini kullanım sıklık grafiği ile ekrana getirdik
plt.hist(dtf["KAPLAMA_CINSI"],title="Yapılan Yol Kaplama Cinsleri")


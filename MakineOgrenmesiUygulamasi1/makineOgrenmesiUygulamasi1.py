import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Dosyanın okunması
df_white=pd.read_csv("winequality-red.csv",sep=";")
df_red=pd.read_csv("winequality-white.csv",sep=";")
# Dosya boyutunun ayarlanması
white=np.ones(df_white.shape[0]).reshape(-1,1)
red=np.zeros(df_red.shape[0]).reshape(-1,1)
# Yeni öznitelik(feature) oluşturulup label isimlerinin yerleştirilmesi
df_white["label"]=white
df_red["label"]=red
# İki farklı verisetinin birleştirilmesi
df=pd.concat((df_white,df_red),axis=0)
df=df.reset_index(drop=True)

#------------------------------------------------------------------------------
# Girdi ve çıktıların bel
x_data=df.drop("label",axis=1)
y=df.label.values.reshape(-1,1)
# MinMax Scaler yapılması yani standartlaştırma
x=(x_data-np.min(x_data))/(np.max(x_data) - np.min(x_data))

# train ve test olarak ikiye bölünmesi verinin
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.3,random_state=71)
# KNN algoritması ile sınıflandırma yapılması
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=4)
knn.fit(x_train,y_train)
y_head=knn.predict(x_test)
# Accuracy değeri => 0.95
from sklearn.metrics import accuracy_score
print("Accuracy: ",accuracy_score(y_test, y_head))
# Confusion(Hata) Matris'inin oluşturulması
from sklearn.metrics import confusion_matrix
print("Matrix:\n",confusion_matrix(y_test, y_head))
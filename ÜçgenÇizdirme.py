import matplotlib.pyplot as plt

aralık1=int(input("İlk aralık gir: "))
aralık2=int(input("İkinci aralık gir: "))
yukseklik=int(input("Yükseklik gir: "))

x=[aralık1,aralık2,(aralık2-aralık1),aralık1]
y=[0,0,yukseklik,0]
plt.plot(x,y)
plt.show()
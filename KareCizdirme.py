import matplotlib.pyplot as plt
ilkDeger=int(input("İlk değer giriniz: "))
ikinciDeger=int(input("İkinci değer giriniz: "))

x=[ilkDeger,ikinciDeger,ikinciDeger,ilkDeger,ilkDeger]
y=[ilkDeger,ilkDeger,ikinciDeger,ikinciDeger,ilkDeger]

plt.plot(x,y)
plt.show()
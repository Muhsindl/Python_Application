import numpy as np

d1 = np.array([])
for i in range(10):
    n1=int(input("Eleman gir: "))
    d1=np.append(d1,n1)

#Aranacak eleman
aranan=int(input("Silinecek sayıyı gir"))

x = np.where(d1 == aranan)
for i in range(len(x)):
    d1 = np.delete(d1, x)

print(d1)
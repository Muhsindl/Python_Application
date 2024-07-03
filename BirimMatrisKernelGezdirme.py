import numpy as np

#Dizi boyutunun kullanıcıdan alınması
diziBoyut=int(input("Matris Boyutu: "))

#Belirtilen boyutta birim matris oluşturulması
Kernel=np.eye(diziBoyut)
array=[]
#Kullanıcıdan matris alınması
for i in range(diziBoyut):
    for j in range(diziBoyut):
        eleman=int(input(f"{i,j}.nci elemanı giriniz: "))
        array.append(eleman)

#Kullanıcı matrisinin numpy dizi dönüşümü
array = np.array(array)
#Kullanıcı matrisine boyut kazandırılması
array = array.reshape(diziBoyut, diziBoyut)
#Matris çarpımı yapılması
matrisCarpimi=array*Kernel
#Matris çarpımının ekranda gösterilmesi
print(matrisCarpimi)
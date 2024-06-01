import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Resmin yolu belirtilir
image=cv.imread("coins.png",0)

#Eşikleme yapılır
_,dst=cv.threshold(image,127,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
copy=dst.copy()
mask=np.zeros((image.shape[0]+2,image.shape[1]+2),np.uint8)
#Taşkın doldurma ile nesneler üzerinde ön işleme yapılır
cv.floodFill(copy, mask, (0,0), 255)
img=cv.bitwise_not(copy)
goruntu=img|dst
#Siyah renkten oluşan görüntü oluşturulur
bgr=np.zeros((image.shape[0],image.shape[1],3),np.uint8)
#Oluşturulan görüntüye görüntü renkleri atanır
bgr[:,:,0]=bgr[:,:,1]=bgr[:,:,2]=image
#Etiketleme yapılır
numLabels,labels,stats,centroids=cv.connectedComponentsWithStats(goruntu)
#Nesnenin seçimi yapılır (Sonsuz döngüden çıkılması istenirse while bloğu kaldırılabilir)
while True:
    for i in range(1,numLabels):
        x=stats[i,0]
        y=stats[i,1]
        w=stats[i,2]
        h=stats[i,3]
        area=stats[i,4]
        cX,cY=centroids[i]
        kopya=bgr.copy()
        #Etrafına yeşil dikdörtgen çizilir
        cv.rectangle(kopya, (x,y), (x+w,y+h),(0,255,0),1)
        #Orta noktasın kırmızı daire çizilir
        cv.circle(kopya,(int(cX),int(cY)),3,(0,0,255),-1)    
        
        maske=np.uint8(labels==i)*255
        #Ekranda seçilmiş nesne ve maske görüntülenir
        cv.imshow("Ekran1",kopya)
        cv.imshow("Maske", maske)
        #1000ms bekleme yapılır
        cv.waitKeyEx(1000)
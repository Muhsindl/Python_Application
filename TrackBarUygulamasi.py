import cv2 as cv
import numpy as np

def nothing(x):
    pass

#Boş bir canvas oluşturuldu
img=np.zeros((512,512,3),dtype=np.uint8)
cv.namedWindow("Image")

#R-G-B renkleri için swicth oluşturuldu
cv.createTrackbar("R", "Image", 0, 255,nothing)
cv.createTrackbar("G", "Image", 0, 255,nothing)
cv.createTrackbar("B", "Image", 0, 255,nothing)
# Kapatma özelliği için switch oluşturuldu
switch="OFF/ON"
cv.createTrackbar(switch, "Image", 0, 1,nothing)

#Sürekli ekranda yenileme gerektiği için sonsuz döngüde yazılacaktır
while True:
    cv.imshow("Image", img)
    # q tuşu ile döngüden çık
    if cv.waitKey(1) & 0xFF==ord("q"):
        break
    r=cv.getTrackbarPos("R", "Image")
    g=cv.getTrackbarPos("G", "Image")
    b=cv.getTrackbarPos("B", "Image")
    switchT=cv.getTrackbarPos(switch, "Image")
    #Eğer switch 0 ise siyah yap
    if switchT==0:
        img[:]=[0,0,0]
    #switch 1 ise renkleri uygula
    else:
        img[:]=b,g,r

cv.destroyAllWindows()


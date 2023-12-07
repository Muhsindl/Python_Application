#Liste verisi
liste=[2,1,4,3,6,5,8,7,9]

for i in range(len(liste)-1):
    tmp=0
    if liste[i]>liste[i+1]:
        tmp=liste[i+1]
        liste[i+1]=liste[i]
        liste[i]=tmp
print(liste)
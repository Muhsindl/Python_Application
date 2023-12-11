def kabarcik(liste):
    sayac=0
    for i in range(len(liste)-1):
        if liste[i]>liste[i+1]:
            liste[i], liste[i+1]=liste[i+1],liste[i]
            sayac=1
    if sayac==0:
        return liste
    else:
        return kabarcik(liste)
dizi=[1,8,3,6,5,4,7,2,9,0]
print(kabarcik(dizi))
# Kullanıcıdan yıl verisi alınıyor
year=int(input("Yıl giriniz: "))
#Kaçıncı yüzyılda olduğumuzu hesaplayan fonksiyon
def yuzYıl(yıl):
    str_yıl=str(yıl)
    
    if(len(str_yıl)<3): #10, 1, 18, 97...
        return 1

    elif(len(str_yıl)==3):
        if(str_yıl[1:3]=="00"): #100, 200, 300, 400 ...
            return int(str_yıl[0])
        else: #190, 250, 425 ...
            return int(str_yıl[0])+1

    else:
        if(str_yıl[2:4]=="00"): #1900, 1800, 1300, 2000..
            return int(str_yıl[:2])
        else:
            return int(str_yıl[:2])+1 
        
print(yuzYıl(year),". yüzyıl")

etkileyenFaktor=int(input("Etkileyen faktör sayısı giriniz: "))
print("."*50)
dersDizi=[]
vizeDizi=[]
finalDizi=[]
ortalamaDizi=[]
etkiOranıVize=int(input("Yüzdelik vize etki oranı giriniz: "))
etkiOranıFinal=int(input("Yüzdelik final etki oranı giriniz: "))

for i in range(etkileyenFaktor):
    ders=input("{}. Dersin adını giriniz: ".format(i+1))
    dersDizi.append(ders)
    
    vize=int(input("{}. Vize notunu giriniz: ".format(i+1)))
    vizeDizi.append(vize)
    
    finall=int(input("{}. Final notunu giriniz: ".format(i+1)))
    finalDizi.append(finall)
    
    print("-"*50)
    
    ortalama=((vizeDizi[i]*etkiOranıVize)/100+(finalDizi[i]*etkiOranıFinal)/100)
    ortalamaDizi.append(ortalama)

print("="*50)
for i in range(etkileyenFaktor):
    print(dersDizi[i]," dersinin ortalaması: {}".format(ortalamaDizi[i]))
    


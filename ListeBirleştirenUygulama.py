liste1=[]
liste2=[]
#Kullanıcıdan liste1 elemanı alma
for i in range(5):
    n=int(input("Liste 1 için eleman gir: "))
    liste1.append(n)
    
#Kullanıcıdan liste2 elemanı alma
for i in range(0,5):
    n=int(input("Liste 2 için eleman gir: "))
    liste2.append(n)
    
liste3=liste1+liste2
print("Listeyi birleştirir ",liste3)
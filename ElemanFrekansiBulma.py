#Kullanıcıdan eleman sayısı alma
eleman=int(input("Eleman sayısı giriniz:"))
s=[]
# Diziye kullanıcıdan eleman ekleme
for i in range(eleman):
    elem=int(input(f"{i+1}nci elemanı giriniz:"))
    s.append(elem)

#Frekans hesaplama ve ekranda gösterme
print("Frekans:")
a=set(s)
for i in a:    
    print(f"{i}:{s.count(i)}")
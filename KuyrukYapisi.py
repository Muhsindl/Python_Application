elemanSayisi=int(input("Lütfen eleman sayısı giriniz: "))
queue=[]
for i in range(elemanSayisi):
    elem=int(input(f"{i+1}nci eleman: "))
    queue.append(elem)

queueStruct=queue[::-1]
# queue.reverse() # Bu fonksiyonda kullanılabilir ters alma işleminde

print(queueStruct.pop()) #FIFO yapıda ilk giren elemanı çıkarır
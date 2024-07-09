#Tablo boyutu girilmesi
sayi=int(input("Tablo boyutu giriniz: "))
"""
Örnek;

Tablo boyutu giriniz: 5
1	2	3	4	5	
2	4	6	8	10	
3	6	9	12	15	
4	8	12	16	20	
5	10	15	20	25
"""
#İstenilen boyutta tablo oluşturur
for i in range(1,sayi+1):
    for j in range(1,sayi+1):
        deger=i*j
        print(deger,end="\t")
    print("")
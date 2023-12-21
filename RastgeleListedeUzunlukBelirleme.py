import numpy as np
# Çarpma işlemi random sayı aralığını arttırır toplama veya çıkarma işlemi ise öteleme yapar.
print("Bir random liste 0-1 arası değerler üretir bunu değiştirmek için sayısal verileri giriniz ")
kaydir=int(input("Kaydırma miktarı giriniz: "))
genislik=int(input("Liste genişletme miktarı giriniz: "))
dizi=(np.random.random((3,2))+kaydir)*genislik #3x2 lik matris oluşturur -1.5 ile 1.5 arasında
print(dizi)
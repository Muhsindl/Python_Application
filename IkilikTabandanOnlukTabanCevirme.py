binary = input("İkilik tabanda sayı giriniz: ")
toplam = 0

for i in range(len(binary)):
    toplam += int(binary[i]) * (2 ** (len(binary) - i - 1))

print(toplam)
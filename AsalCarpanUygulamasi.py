# Kullanıcıdan sayı alınması
n = int(input("Bir sayı girin: "))  

# Ekran çıktısı
print(f"{n} sayısının asal çarpanları: ", end="")

# Asal çarpanların bulunması
for i in range(2,n):
    if n % i == 0:  # Eğer i, n'i tam bölüyorsa
        print(i, end=" ")
        n //= i

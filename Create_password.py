import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

kac_harf = int(input("Kaç tane harf olsun şifrenizde?\n"))
kac_sembol = int(input("Kaç tane sembol olsun şifrenizde?\n"))
kac_sayi = int(input("Kaç tane sayi olsun şifrenizde?\n"))

#Kolay yöntemde alacağımız çıktı.

sifre = ""

for i in range(kac_harf):
    random_harf = random.choice(letters)
    sifre += random_harf

for i in range(kac_sembol):
    random_sembol = random.choice(symbols)
    sifre += random_sembol

for i in range(kac_sayi):
    random_sayi = random.choice(numbers)
    sifre += random_sayi

print(sifre)

#Zor yöntemde alacağımız çıktı.

rastgele_sifre = letters + numbers + symbols

uzunluk_deger = int(input("Kaç karakterli olsun? = "))

sifre = "".split()

for i in range(uzunluk_deger):
    sifre += random.choice(rastgele_sifre)

#Gömülü metot

sifre_karistir = sifre.copy()
random.shuffle(sifre_karistir)
print(''.join(sifre_karistir))
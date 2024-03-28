import math

# Definiramo listu tocaka
tocke = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Izracunamo aritmetictu sredinu
arit_sredina = sum(tocke) / len(tocke)

# Izračunamo standardnu devijaciju
s = sum((x - arit_sredina) ** 2 for x in tocke) / len(tocke)
std_devijacija = math.sqrt(s)

print("Aritmetička sredina:", arit_sredina)
print("Standardna devijacija:", std_devijacija)


import numpy as np

tocke = [2, 4, 5, 7, 9, 10, 11, 13, 14, 15]

arit_sredina = np.mean(tocke)
std_devijacija = np.std(tocke)

print("Aritmetička sredina: ", arit_sredina)
print("Standardna devijacija: ", std_devijacija)
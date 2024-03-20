import numpy as np
import matplotlib.pyplot as plt

F = float(input("Unesite iznos sile (N): "))
m = float(input("Unesite masu čestice (kg): "))

v0 = F / m
t = np.linspace(0, 10, 100)  # Od 0 do 10 sekundi, 100 točaka
x = v0 * t
v = np.full_like(t, v0)
a = np.zeros_like(t)
plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
plt.plot(t, x, 'b-')
plt.title('x - t graf')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Pomak (m)')

plt.subplot(3, 1, 2)
plt.plot(t, v, 'g-')
plt.title('v - t graf')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Brzina (m/s)')

plt.subplot(3, 1, 3)
plt.plot(t, a, 'r-')
plt.title('a - t graf')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Ubrzanje (m/s^2)')

plt.tight_layout()
plt.show()
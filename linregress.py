import numpy as np
import matplotlib.pyplot as plt

m=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
phi=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

a=((sum(m)/len(m))*(sum(phi)/len(phi)))/((sum(phi)/len(phi))**2)
print(a)

x = []
y = []
for i in range(0, 200):
    xp = i*0.01
    yp = a*xp
    x.append(xp)
    y.append(yp)

plt.plot(x, y)
plt.plot(phi, m, "bo")
plt.show()
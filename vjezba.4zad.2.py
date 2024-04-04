import Particle as P
import numpy as np
import matplotlib.pyplot as plt
p = Particle(10, 60, 0, 0)

#analiticko rj
k = np.radians(60)
domet = 100*np.sin(2*k)/9.81 #formula za analiticko rjesenje iz of1 (ne treba se racunati za svaki dt, jer ovo nije numericko)
#print(domet)

#numericko rjesenje
num = []
vri = np.linspace(0.01, 0.2, 999)
for dt in vri:
    a = p.range(dt)
    num.append(a)
    p.reset()
#print(num)

er=[]
for i in range(len(num)):
    gr=((abs(domet-num[i]))/domet)*100
    er.append(gr)
#print(er)

plt.plot(vri, er)
plt.title('Ovisnost odstupanja o koraku dt')
plt.xlabel('dt [s]')
plt.ylabel('Odstupanje [%]')
plt.show()
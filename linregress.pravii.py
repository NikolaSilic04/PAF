import matplotlib.pyplot as plt
import numpy as np
M=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #mjerna jedinica za moment sile Nm
φ=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] # mjern jedinica za kut zakretanja rad
xy=[]
x=[]
y=[]
n=len(M)
for i in range(n):
    c=M[i]*φ[i]
    xy.append(c)
    b=φ[i]**2
    x.append(b)
    a=M[i]**2
    y.append(a)
bro=np.mean(xy)
naz=np.mean(x)
moment=np.mean(y)
Dt=bro/naz
std=np.sqrt(1/6*((moment/naz)-Dt**2))
#Rezultati koji su dobiveni koristenjem formula u Zdk4.
print('Rezultati koji su dobiveni koristenjem formula u Zdk4')
print('Modul torzije aluminijske sipke je {}.'.format(Dt))
print('Standardna devijacija iznosi {}.'.format(std))
#formula linearne regresije
k, n = np.polyfit(φ, M, deg=1)
reg_lin = k*np.array(φ) + n
#graf
plt.plot(φ, M, 'o', label='podaci')
plt.plot(φ, reg_lin, label='linearna regresija')
plt.title('Graf linearnog pravca za dani skup podataka')
plt.xlabel('φ [rad]')
plt.ylabel('M [Nm]')
plt.legend()
plt.show()
#Razlog zasto umjesto len(M) pisem 6.
#if len(M)==len(φ):
#    print('true, len je {}'.format(len(M)))
#else:
#    print('false')
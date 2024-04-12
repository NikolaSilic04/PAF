import calculus as c
import matplotlib.pyplot as plt
import numpy as np

def kubna_f(x):
    return 5*(x**3)-2*(x**2)+2*x-3

def trig_f(x):
    return np.sin(x)

def d1kubna_f(x):
    return 15*(x**2)-4*x+2

de=c.derivacije(a=-2,b=2,x=5,dx=0.1)
tr=de.derivacijaII(f=trig_f)
print('tocke za trigonometrijsku funkciju iznose {}'.format(tr))
u=de.derivacijaI(f=kubna_f,IIPmeth=True)
print('Derivacija u jednoj tockipomocu TwoPoint metode iznosi {}'.format(u))
#Crtanje grafa derivacije 
tocke = np.linspace(-2, 2, 100)
funkcija = kubna_f(tocke)
derivacija_num = de.derivacijaII(kubna_f)[1]
derivacija_ana = d1kubna_f(tocke)
d=c.derivacije(a=-2,b=2,x=5,dx=0.01)
deriv_num2=d.derivacijaII(kubna_f)[1]

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(tocke, derivacija_ana, linestyle='-', linewidth=2.5, color='black',label='Analiticka derivacija')
ax.plot(de.derivacijaII(kubna_f)[0], derivacija_num, 'o',markersize=4,color='green' ,label='Numericka derivacija pri koraku derivacije 0.1')
ax.plot(d.derivacijaII(kubna_f)[0], deriv_num2, 'o',markersize=4,color='red' ,label='Numericka derivacija pri koraku derivacije 0.01')
ax.set_title('Derivacija funkcije')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.legend()
plt.show()
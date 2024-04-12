import calculus as cal
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def fzint(x):
    return 2*x**2+3

analiticko_rj = []

# Racunanje analiticke integracije
# definirajmo simbole
t = sp.Symbol('t')
# definirajmo funkciju koju zelimo integrirati
f = 2*t**2 + 3
# definirajmo granice integracije
dgr = 0
ggr = 1
# izvrsimo integraciju
F = sp.integrate(f, (t, dgr, ggr)) #rezultat iznosi 11/3
g = float(F)
analiticko_rj.append(g)

i = cal.integracije(a=0., b=1., n=50.)
granicni_integrali = i.integracijaI(f=fzint)
print('test')
print('Gornja granica iznosi: '.format(granicni_integrali[1]))
print('Donja granica iznosi: '.format(granicni_integrali[0]))

trp = i.integracijaII(f=fzint)
print('Kroz trapeznu formulu iznos integrala je: {}.'.format(trp))
gornja=[]
donja=[]
trap_form=[]
n=np.linspace(15,100,25)
for l in n:
    i = cal.integracije(a=0., b=1., n=int(l))
    c=i.integracijaI(f=fzint)
    gornja.append(c[0])
    donja.append(c[1])
    t=i.integracijaII(f=fzint)
    trap_form.append(t)
plt.plot(n, donja, 'o',color='black' ,label="Donja granica")
plt.plot(n, gornja, 'o',color='red' ,label="Gornja granica")
plt.plot(n, trap_form, 'o',color='blue' ,label="Trapezna formula")
plt.plot(n, [analiticko_rj[0]]*len(n), '-', color='magenta', label="Analiticko rjesenje")
plt.title('Upotreba integracije')
plt.xlabel('Broj koraka N')
plt.ylabel('Iznos integracije')
plt.legend()
plt.show()
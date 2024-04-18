import Harmonic_oscillator as ho 
import numpy as np 
import matplotlib.pyplot as plt 

hosn=ho.HarmonicOscillator(x=3,v=2,k=1,dt=200,m=3)
ha = ho.HarmonicOscillator(x=3, v=2, k=1, dt=0.01, m=3)
hb = ho.HarmonicOscillator(x=3, v=2, k=1, dt=0.001, m=3)
hc = ho.HarmonicOscillator(x=2, v=2, k=1, dt=0.16, m=3)

def Analiticko_rj(t_kr):
    A = np.sqrt((hosn.x[0])**2+((hosn.m/hosn.k)*(hosn.v[0])**2))
    fi = np.arcsin(hosn.x[0]/A)
    omega=np.sqrt(hosn.k/hosn.m)
    arj=[]
    vrijeme=[]
    for t in np.linspace(0,t_kr,hosn.dt):
        vrijeme.append(t)
        x=A*np.sin(omega*t+fi)
        arj.append(x)
    return vrijeme, arj

def Preciznost(t_kr):
    arj, vrijeme = Analiticko_rj(t_kr=t_kr)
    plt.plot(arj, vrijeme, label='analiticko rjesenje', color='magenta')
    plt.title('Preciznost')
    plt.plot(ha.Izracun(t=20)[0], ha.Izracun(t=20)[1], 'o', color='red',markersize='0.8')
    plt.plot(hb.Izracun(t=20)[0], hb.Izracun(t=20)[1], 'o', color='blue',markersize='0.1')
    plt.plot(hc.Izracun(t=20)[0], hc.Izracun(t=20)[1], 'o', color='green',markersize='1')
    plt.xlabel('t [s]')
    plt.ylabel('x [m]')
    plt.legend(['Analiticko', 'dt = 0.01', 'dt = 0.001', 'dt = 0.16'])
    plt.show()

Preciznost(t_kr=20)
########################################################################################################
#Analiticki i numericki period(2.Zdk)
#Analitički period
#T=2*np.pi/omega
#omega=np.sqrt(k/m)
hosn = ho.HarmonicOscillator(x=3,v=2,k=1,dt=200,m=3)
ha = ho.HarmonicOscillator(x=3, v=2, k=1, dt=0.01, m=3)
hb = ho.HarmonicOscillator(x=3, v=2, k=1, dt=0.001, m=3)
hc = ho.HarmonicOscillator(x=2, v=2, k=1, dt=0.16, m=3)
hd = ho.HarmonicOscillator(x=2, v=2, k=1, dt=0.26, m=3)
he= ho.HarmonicOscillator(x=2, v=2, k=1, dt=0.24, m=3)
hf = ho.HarmonicOscillator(x=2, v=2, k=1, dt=0.32, m=3)
hg = ho.HarmonicOscillator(x=2, v=2, k=1, dt=0.02, m=3)
hh = ho.HarmonicOscillator(x=2, v=2, k=1, dt=0.2, m=3)
hi = ho.HarmonicOscillator(x=2, v=2, k=1, dt=0.12, m=3)
hj = ho.HarmonicOscillator(x=2, v=2, k=1, dt=0.69, m=3)


def Analiticko_rj(t_kr):
    A = np.sqrt((hosn.x[0])**2+((hosn.m/hosn.k)*(hosn.v[0])**2))
    fi = np.arcsin(hosn.x[0]/A)
    omega=np.sqrt(hosn.k/hosn.m)
    arj=[]
    vrijeme=[]
    for t in np.linspace(0,t_kr,hosn.dt):
        vrijeme.append(t)
        x=A*np.sin(omega*t+fi)
        arj.append(x)
    return vrijeme, arj

def Preciznost(t_kr):
    arj, vrijeme = Analiticko_rj(t_kr=t_kr)
    plt.plot(arj, vrijeme, label='analiticko rjesenje',color='magenta')
    plt.title('Preciznost analitickog rjesenja za x-t graf')
    plt.plot(ha.Izracun(t=20)[0], ha.Izracun(t=20)[1], 'o', color='blue',markersize='0.8')
    plt.plot(hb.Izracun(t=20)[0], hb.Izracun(t=20)[1], 'o', color='orange',markersize='0.1')
    plt.plot(hc.Izracun(t=20)[0], hc.Izracun(t=20)[1], 'o', color='green',markersize='1')
    plt.xlabel('t [s]')
    plt.ylabel('x [m]')
    plt.legend(['Analiticko', 'dt = 0.01', 'dt = 0.001', 'dt = 0.16'])
    plt.show()

def Analiticki_Period(t_kra):
    omega=np.sqrt(hosn.k/hosn.m)
    T_an=[]
    T=2*np.pi/omega
    T_an.append(T)
    return T_an

def Preciznost_perioda():
    numericki_rezultati=[]
    numericki_rezultati.append(ha.Numericki_Period())
    numericki_rezultati.append(hb.Numericki_Period())
    numericki_rezultati.append(hc.Numericki_Period())
    numericki_rezultati.append(hd.Numericki_Period())
    numericki_rezultati.append(he.Numericki_Period())
    numericki_rezultati.append(hf.Numericki_Period())
    numericki_rezultati.append(hg.Numericki_Period())
    numericki_rezultati.append(hh.Numericki_Period())
    numericki_rezultati.append(hi.Numericki_Period())
    numericki_rezultati.append(hj.Numericki_Period())
    koraci=np.arange(0,1,0.1)
    plt.axhline(Analiticki_Period(t_kra=20),color='orange')
    plt.plot(koraci, numericki_rezultati, 'o', color='black',markersize='5')
    plt.xlabel('vremenski korak dt')
    plt.ylabel('Numericki period')
    plt.title('Preciznost numerickog perioda')
    plt.legend(['Analiticki period', 'Numericki periodi'])
    plt.show()
Preciznost_perioda()
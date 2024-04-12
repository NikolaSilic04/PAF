#1.zadatak########################


import numpy as np

class derivacije:
    def __init__(self, a, b, x, dx):
        self.a = a
        self.b = b
        self.x = x
        self.dx = dx
        
    def derivacijaI(self, f, IIPmeth=True):#derivacija sa twopoint i three point metodom
        '''
        Ova funkcija iz klase derivacije racuna derivaciju pomocu ThreePointMetod kao zadanom metodom te sa TwoPointmethod kao izbornom 
        metodom ako netko unese ista drugo osim True na mjestu atributa IIPmeth
        '''
        if IIPmeth:
            der = (f(self.x)-f(self.x-self.dx))/self.dx
        else:
            der = (f(self.x+self.dx)-f(self.x-self.dx))/(2*self.dx)
        return der
    
    def derivacijaII(self, f, IIPmeth=True):#derivacija sa granicama
        '''
        Ova funkcija iz klase derivacije racuna derivaciju uzimajuci u obzir gornju i donju granicu derivacije kao i 
        funkciju te tocku u kojoj ce derivacija biti izvrsena. Funkcija vraca listu tocaka u kojima ce biti izvrsena numericka derivacija
        '''
        tocke_derivacije=[]
        N=np.linspace(self.a,self.b,100)
        for ele in N:
            if IIPmeth:
                der=(f(ele)-f(ele-self.dx))/self.dx
                tocke_derivacije.append(der)
            else:
                der=(f(ele+self.dx)-f(ele-self.dx))/(2*self.dx)
                tocke_derivacije.append(der)
        return N,tocke_derivacije
    
    
#2.zadatak##########################################################
class integracije:
    def __init__(self,a,b,n):
        self.a = a
        self.b = b
        self.n = n
        self.dx = (b - a) / n

    def integracijaI(self, f):#integracija za gornji i donji integral
        '''
        Ova funkcija iz klase integracije racuna gornji i donji integral. Tocnije, gornju i donju granicu.
        '''
        gornja_gran = []
        donja_gran = []
        dx = np.linspace(self.a, self.b, self.n+1)
        N = len(dx)-1
        for i in range(N):
            F_U = f(dx[i+1]) * self.dx
            gornja_gran.append(F_U)
            F_L = f(dx[i]) * self.dx
            donja_gran.append(F_L)
        return sum(gornja_gran), sum(donja_gran)
    
    def integracijaII(self, f):#integracija pmocu formule za trapezni integral
        '''
        Ova funkcija iz klase integracije racuna numericki rezultat pomocu trapezne integracije.
        '''
        num=[]
        dx=np.linspace(self.a, self.b, self.n+1)
        N=len(dx)-1
        for j in range(N):
            trap=(f(dx[j])+f(dx[j+1]))*abs(self.dx)/2
            num.append(trap)
        return sum(num)
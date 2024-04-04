import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,v_0,Θ,y,x):
        self.v_0 = v_0
        self.Θ = np.radians(Θ)
        self.x = x #potrebno je dodati self.x i self.y da bismo ih mogli dolje upotrijebiti kod funkcije reset
        self.x_0 = [x]
        self.y = y
        self.y_0 = [y]
        self.vy = [v_0*np.sin(self.Θ)]
        self.vx = [v_0*np.cos(self.Θ)]
    
    def reset(self):
        self.x_0 = [self.x] #kod resetiranja moramo staviti da je sada jedina vrijednost jednaka onoj pocetnoj vrijednosti, a ne nuli
        self.y_0 = [self.y] #ako prilikom resetiranja stavimo da je sve jednako nula, onda izgubimo pocetne uvjete i vise ne mozemo nista racunati
        self.vy = [self.v_0*np.sin(self.Θ)]
        self.vx = [self.v_0*np.cos(self.Θ)]

    def __move(self, dt):
        g = 9.81
        self.x_0.append(self.x_0[-1]+self.vx[-1]*dt)
        self.y_0.append(self.y_0[-1]+self.vy[-1]*dt)
        self.vy.append(self.vy[-1]-g*dt)
        self.vx.append(self.vx[-1])

  
    def range(self, dt):
        while self.y_0[-1] >= 0:
            self.__move(dt)
        return self.x_0[-1]
    
    def plot_trajectory(self, dt):
        while self.y_0[-1] >= 0: #da bismo plotali proizvoljnu putanju dopustamo korisniku da unese dt koji zeli
            Particle.__move(self,dt)
        plt.plot(self.x_0, self.y_0)
        plt.title('Trenutno stanje cestice')
        plt.xlabel('x[m]')
        plt.ylabel('y[m]')
        plt.show()
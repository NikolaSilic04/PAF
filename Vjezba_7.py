import matplotlib.pyplot as plt
import numpy as np

class Projectile:
    def __init__(self, x, y, v, th, m, dt, t_fin, Cd, A):
        self.A=A
        self.t_fin=t_fin
        self.v = v
        self.dt = dt
        self.Cd = Cd
        self.m = m
        self.th = np.radians(th)
        self.x = [x]
        self.y = [y]
        self.g = 9.81  # ubrzanje gravitacije (m/s^2)
        self.rho = 1.225  # gustoća zraka (kg/m^3) na nadmorskoj visini
        self.vx = [self.v * np.cos(self.th)]
        self.vy = [self.v * np.sin(self.th)]
        self.ax = [-abs(self.rho * self.Cd * self.A * (self.vx[-1])**2 / (2 * self.m))]
        self.ay = [-self.g - abs(self.rho * self.Cd * self.A * (self.vy[-1])**2 / (2 * self.m))]
    
    def Euler(self):
        for i in np.arange(0,self.t_fin,self.dt):
            # Izračunajte novi položaj projektila
            self.x.append(self.x[-1] + (self.vx[-1] * self.dt))
            self.y.append(self.y[-1] + (self.vy[-1] * self.dt))
            # Izračunajte novu brzinu projektila
            self.vx[-1] += self.ax[-1] * self.dt
            self.vy[-1] += self.ay[-1] * self.dt
            #Izracun akceleracije
            self.ax = [-abs(self.rho * self.Cd * self.A * (self.vx[-1])**2 / (2 * self.m))]
            self.ay = [-self.g - abs(self.rho * self.Cd * self.A * (self.vy[-1])**2 / (2 * self.m))]
            if self.y[-1]<0:
                break
    
    

    def Runge_Kutta(self):
        tim = np.arange(0, self.t_fin, self.dt)
        for i in tim:
            kvx=[(-np.sign(self.vx[-1])*(self.rho*self.Cd*self.A/(2*self.m))*(self.vx[-1])**2)*self.dt]
            kvy=[((-self.g-np.sign(self.vy[-1])*(self.rho*self.Cd*self.A/(2*self.m))*(self.vy[-1])**2)*self.dt)]
            kx = [self.vx[-1]*self.dt]
            ky = [self.vy[-1]*self.dt]
            if self.y[-1] < 0:
                break

            for j in range(len(tim)-1):
                kvx.append((-np.sign(self.vx[-1])*(self.rho*self.Cd*self.A/(2*self.m))*(self.vx[-1])**2)*self.dt)
                kvy.append((-self.g-np.sign(self.vy[-1]+kvy[-1])*(self.rho*self.Cd*self.A/(2*self.m))*(self.vy[-1]+kvy[-1])**2)*self.dt)
                kx.append((self.vx[-1]+kvx[-1])*self.dt)
                ky.append((self.vy[-1]+kvy[-1])*self.dt)

            self.vx.append(self.vx[-1]+(kvx[0]+2*kvx[1]+2*kvx[2]+kvx[3])/6)
            self.vy.append(self.vy[-1]+(kvy[0]+2*kvy[1]+2*kvy[2]+kvy[3])/6)
            self.x.append(self.x[-1]+(kx[0]+2*kx[1]+2*kx[2]+kx[3])/6)
            self.y.append(self.y[-1]+(ky[0]+2*ky[1]+2*ky[2]+ky[3])/6)

    def VratInfo(self):
        print('v={}'.format(self.v))
        print('dt={}'.format(self.dt))
        print('m={}'.format(self.m))
        print('x={}'.format(self.x)) 
        print('y={}'.format(self.y))
        print('vx={}'.format(self.vx))
        print('vy={}'.format(self.vy))
        print('ax={}'.format(self.ax))
        print('ay={}'.format(self.ay))

    def Grafovi(self, Nacin,P):
        if Nacin=='Euler':
            Projectile.Euler(self)
            plt.plot(self.x, self.y)
            plt.title('x-y graf')
            plt.xlabel('x [m]')
            plt.ylabel('y [m]')
            if P==True:
                plt.show()
        if Nacin=='RungeKutta':
            Projectile.Runge_Kutta(self)
            plt.plot(self.x, self.y)
            plt.title('x-y graf')
            plt.xlabel('x [m]')
            plt.ylabel('y [m]')
            if P==True:
                plt.show()


p1=Projectile(x=0,y=0,v=50,th=45,m=2,dt=0.01,t_fin=20,Cd=0.47,A=0.02)
p2=Projectile(x=0,y=0,v=50,th=45,m=2,dt=0.001,t_fin=20,Cd=0.47,A=0.02)
p3=Projectile(x=0,y=0,v=50,th=45,m=2,dt=0.2,t_fin=20,Cd=0.47,A=0.02)
p4=Projectile(x=0,y=0,v=50,th=45,m=2,dt=0.01,t_fin=20,Cd=0,A=0.02)
p5=Projectile(x=0,y=0,v=50,th=45,m=2,dt=0.01,t_fin=20,Cd=0.47,A=0.02)



p1.Grafovi(Nacin='Euler',P=False)
p2.Grafovi(Nacin='Euler',P=False)
p3.Grafovi(Nacin='Euler',P=False)
p4.Grafovi(Nacin='Euler',P=False)
p5.Grafovi(Nacin='RungeKutta',P=False)

plt.legend(['dt = 0.01', 'dt = 0.001', 'dt = 0.2','dt=0.01, Cd = 0','dt=0.01, Runge-Kutta metoda'])
plt.show()
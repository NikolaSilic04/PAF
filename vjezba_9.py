import numpy as np
import matplotlib.pyplot as plt

class Suncev_sustav:
    def __init__(self, au, mc1, mc2, v1, r1, v2, r2, t_kraj, dt):
        self.au = au * 1.486 * 10 ** 11  # m
        self.mc1 = mc1  # kg   
        self.mc2 = mc2  # kg
        self.G = 6.67408 * 10 ** (-11)  # Nm^2/kg^2
        self.v1 = [v1]
        self.r1 = [r1]
        self.v2 = [v2]
        self.r2 = [r2]
        self.t_kraj = t_kraj
        self.dt = dt
        self.a1 = []
        self.a2 = []


    def VratInfo(self):
        print('a1 =', self.a1)
        print('a2 =', self.a2)
        print('r1 =', self.r1)
        print('r2 =', self.r2)
        print('v1 =', self.v1)
        print('v2 =', self.v2)
        print('au =', self.au)
        print('dt =', self.dt)

    def Izracun(self):
        for i in np.arange(0, self.t_kraj, self.dt):
            d1 = self.r1[-1] - self.r2[-1]
            d2 = self.r2[-1] - self.r1[-1]
            self.a1.append(-self.G * self.mc2 * d1 / (np.sqrt(np.dot(d1, d1)) ** 3))
            self.v1.append(self.v1[-1] + self.a1[-1] * self.dt)
            self.r1.append(self.r1[-1] + self.v1[-1] * self.dt)
            self.a2.append(-self.G * self.mc1 * d2 / (np.sqrt(np.dot(d2, d2)) ** 3))
            self.v2.append(self.v2[-1] + self.a2[-1] * self.dt)
            self.r2.append(self.r2[-1] + self.v2[-1] * self.dt)
    
    def Simulacija(self):
        self.Izracun()
        x1 = []
        y1 = []
        x2 = []
        y2 = []

        for r in self.r1:
            x1.append(r[0])
            y1.append(r[1])

        for r in self.r2:
            x2.append(r[0])
            y2.append(r[1])

        plt.plot(x1, y1, label='Sunce',marker='o',markersize='1',color='red')
        plt.plot(x2, y2, label='Zemlja',color='blue')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Suncev sustav simulacija')
        plt.legend()
        plt.show()

n = Suncev_sustav(au=1, mc1 = 1.989 * 10 ** 30, mc2=5.9742 * 10 ** 24, v1=np.array([0, 0]), r1=np.array([0, 0]), v2=np.array([0, 29783]),r2=np.array([1.486 * 10 ** 11, 0]), t_kraj=31536000, dt=86400)
n.Simulacija()
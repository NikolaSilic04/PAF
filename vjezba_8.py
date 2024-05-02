import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Nabijene_cestice:
    def __init__(self, E, B, v, m, q, x, dt, t_kr):
        self.E = E
        self.B = B
        self.v = [v]
        self.x = [x]
        self.m = m
        self.q = q
        self.dt = dt
        self.t_kr = t_kr        
        self.a = []

    def PrintInfo(self):
        print('E={}'.format(self.E))
        print('B={}'.format(self.B))
        print('v={}'.format(self.v))
        print('q={}'.format(self.q))
        print('dt={}'.format(self.dt))
        print('a={}'.format(self.a))
        print('x={}'.format(self.x))

    def Euler(self):
        for i in np.arange(0, self.t_kr, self.dt):
            self.a = (self.q / self.m) * (self.E + np.cross(self.v[-1], self.B))
            self.v.append(self.v[-1] + self.a * self.dt)
            self.x.append(self.x[-1] + self.v[-1] * self.dt)


    def Simulacija(self, *args):
        for i, obj in enumerate([self, *args]):
            obj.Euler()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Prikaz svih grafova
        colors = ['blue', 'red']
        names = ['Elektron', 'pozitron']
        for i, obj in enumerate([self, *args]):
            x = []
            y = []
            z = []
            for pos in obj.x:
                x.append(pos[0])
                y.append(-pos[1])
                z.append(pos[2])
            ax.plot(x, y, z, color=colors[i], label=names[i])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()

    def Prec_Euler(self, *args):
        for i, obj in enumerate([self, *args]):
            obj.Euler()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        colors = ['blue', 'red','Green']
        names = ['dt=0.01', 'dt=0.20','dt=0.15']
        for i, obj in enumerate([self, *args]):
            x = []
            y = []
            z = []
            for pos in obj.x:
                x.append(pos[0])
                y.append(pos[1])
                z.append(pos[2])
            ax.plot(x, y, z, color=colors[i], label=names[i])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()

p = Nabijene_cestice(E=np.array((0, 0, 0)), B=np.array((0, 0, 1)), v=np.array((0.1, 0.1, 0.1)), m=1, q=1, x=np.array((0, 0, 0)), dt=0.01, t_kr=20)
e = Nabijene_cestice(E=np.array((0, 0, 0)), B=np.array((0, 0, 1)), v=np.array((0.1, 0.1, 0.1)), m=1, q=-1, x=np.array((0, 0, 0)), dt=0.01, t_kr=20)

e0 = Nabijene_cestice(E=np.array((0, 0, 0)), B=np.array((0, 0, 1)), v=np.array((0.1, 0.1, 0.1)), m=1, q=-1, x=np.array((0, 0, 0)), dt=0.01, t_kr=20)
e1 = Nabijene_cestice(E=np.array((0, 0, 0)), B=np.array((0, 0, 1)), v=np.array((0.1, 0.1, 0.1)), m=1, q=-1, x=np.array((0, 0, 0)), dt=0.20, t_kr=20)
e2 = Nabijene_cestice(E=np.array((0, 0, 0)), B=np.array((0, 0, 1)), v=np.array((0.1, 0.1, 0.1)), m=1, q=-1, x=np.array((0, 0, 0)), dt=0.15, t_kr=20)

e.Simulacija(p)
plt.title('Usporedba gibanja elektrona i pozitrona')
plt.show()
e0.Prec_Euler(e1,e2)
plt.title('Provjera preciznosti Eulerove metode (preko elektrona)')
plt.show()
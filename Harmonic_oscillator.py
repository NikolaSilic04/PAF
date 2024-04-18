import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, x, v, k, dt, m):
        self.m = m
        self.k = k
        self.t = [0] # početno vrijeme
        self.x = [x] # početni položaj
        self.v = [v] # početna brzina
        self.a = [-self.k * self.x[-1] / self.m]
        self.dt=dt

    def Izracun(self,t):
        while self.t[-1] < t:
            self.a.append(-self.k / self.m * self.x[-1])
            self.v.append(self.v[-1] + self.a[-1] * self.dt)
            self.x.append(self.x[-1] + self.v[-1] * self.dt)
            self.t.append(self.t[-1] + self.dt)
        return self.t,self.x,self.v,self.a

    def Informacije(self):
        print('vremenski intervali: {}'.format(self.t))
        print('polozaji: {}'.format(self.x))
        print('brzina: {}'.format(self.v))
        print('akceleracija: {}'.format(self.a))

    def Grafovi(self, t):
        HarmonicOscillator.Izracun(self, t)
        fig, ax = plt.subplots(nrows=3, ncols=1)

        ax[0].plot(self.t, self.x)
        ax[0].set_title('x-t graf')
        ax[0].set_xlabel('t [s]')
        ax[0].set_ylabel('x [m]')

        ax[1].plot(self.t, self.v)
        ax[1].set_title('v-t graf')
        ax[1].set_xlabel('t [s]')
        ax[1].set_ylabel('v [m/s]')

        ax[2].plot(self.t, self.a)
        ax[2].set_title('a-t graf')
        ax[2].set_xlabel('t [s]')
        ax[2].set_ylabel('a [m/s^2]')

        plt.show()

    def Numericki_Period(self):
        HarmonicOscillator.Izracun(self, 2 * np.pi * np.sqrt(self.m / self.k))
        t0 = t1 = None
        for i in range(len(self.x)):
            if not t0 and self.x[0]/self.x[i] < 0:
                t0 = self.t[i]
            elif t0 and self.x[0]/self.x[i] > 0:
                t1 = self.t[i]
                break
        if t0 is not None and t1 is not None:
            return 2. * (t1 - t0)
        else:
            return None
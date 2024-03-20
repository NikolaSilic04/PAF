import matplotlib.pyplot as plt
import numpy as np
v0=float(input('Unesi početnu brzinu u m/s: '))
k=float(input('Unesi kut u stupnjevima:'))
pi=np.pi
rad = k*(pi/180)
g=9.81

#za crtanje x-y grafa
t = np.arange(0, 10, 0.2)
x = v0 * np.cos(rad) * t
y = v0 * np.sin(rad) * t - 0.5 * g * t**2

plt.plot(x, y)
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('x-y graf')
plt.show()

#za crtanje x-t grafa
t = np.arange(0, 10, 0.2)
x = v0 * np.cos(rad) * t

plt.plot(t, x)
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.title('x-t graf')
plt.show()

#za crtanje y-t grafa
t = np.arange(0, 10, 0.2)
y = v0 * np.sin(rad) * t - 0.5 * g * t**2

plt.plot(t, y)
plt.xlabel('t [s]')
plt.ylabel('y [m]')
plt.title('y-t graf')
plt.show()
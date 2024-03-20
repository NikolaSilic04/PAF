def jednoliko_gibanje(F,m,dt):
    import matplotlib.pyplot as plt
    import numpy as np
    
    a = F/m
    v0 = 0
    x0 = 0
    
    t = np.arange(0, 10, dt)
    v = [v0]
    x = [x0]
    akc = [a]
    b=len(t)-1
    for i in range(b):
        dv = akc[-1] * dt
        v_i = v[-1] + dv
        v.append(v_i)
        
        dx = v[-1] * dt
        x_i = x[-1] + dx
        x.append(x_i)
        
        akc.append(a)
        
    plt.plot(t, v)
    plt.title('v-t graf')
    plt.xlabel('t [s]')
    plt.ylabel('v [m/s]')
    plt.show()
    
    plt.plot(t, x)
    plt.title('x-t graf')
    plt.xlabel('t [s]')
    plt.ylabel('x [m]')
    plt.show()
    
    plt.plot(t, akc)
    plt.title('a-t graf')
    plt.xlabel('t [s]')
    plt.ylabel('a [m/s^2]')
    plt.show()

    

def kosi_hitac(v0,k,dt):
    import matplotlib.pyplot as plt
    import numpy as np
    pi=np.pi
    rad = k*(pi/180)
    g=9.81

    t = np.arange(0, 10, 0.2)
    x = v0 * np.cos(rad) * t
    y = v0 * np.sin(rad) * t - 0.5 * g * t**2
    
    plt.plot(x, y)
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.title('x-y graf')
    plt.show()
    
    t = np.arange(0, 10, dt)
    x = v0 * np.cos(rad) * t
    
    plt.plot(t, x)
    plt.xlabel('t [s]')
    plt.ylabel('x [m]')
    plt.title('x-t graf')
    plt.show()
    

    t = np.arange(0, 10, 0.2)
    y = v0 * np.sin(rad) * t - 0.5 * g * t**2
    
    plt.plot(t, y)
    plt.xlabel('t [s]')
    plt.ylabel('y [m]')
    plt.title('y-t graf')
    plt.show()
import math
import matplotlib.pyplot as plt  
from matplotlib import animation      
g=9.8 
#calculate the trajectory
def Damped(omega0,theta0,q,l,T):#q is related to damping force, while FD and omegaD is related to the driving force. the length of the rod is l.T is the interest time.
    dt=0.001
    t=0
    omega,theta = omega0,theta0
    motion=[[]for i in range(3)]
    motion[0].append(omega)
    motion[1].append(theta)
    motion[2].append(t)
    while t<= T:
        omega = omega+(-g*theta/l-q*omega)*dt
        theta = theta+omega*dt
        t = t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion

#Fig.1.damped pendulum without driving force
d=Damped(0,0.5,1,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=1')
d=Damped(0,0.5,3,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=3')
d=Damped(0,0.5,9.8**0.5*2,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q='+r'$2\sqrt{g/l}$')
d=Damped(0,0.5,10,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=10')
d=Damped(0,0.5,30,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=30')
plt.xlim(0,10)
plt.grid(True,color='k')
plt.title('Damped Pendulum')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.legend()
plt.show()

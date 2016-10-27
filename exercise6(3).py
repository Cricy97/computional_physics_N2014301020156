import math
import matplotlib.pyplot as plt  
from matplotlib import animation      
g=9.8 
#calculate the trajectory
def DampedDriven(omega0,theta0,q,FD,omegaD,l,T):#q is related to damping force, while FD and omegaD is related to the driving force. the length of the rod is l.T is the interest time.
    dt=0.001
    t=0
    omega,theta = omega0,theta0
    motion=[[]for i in range(3)]
    motion[0].append(omega)
    motion[1].append(theta)
    motion[2].append(t)
    while t<= T:
        omega = omega+(-g*theta/l-q*omega+FD* math.sin(omegaD*t))*dt
        theta = theta+omega*dt
        t = t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion

d=DampedDriven(0,0.2,1,0.1,1,1,20)#(omega0,theta0,q,FD,omegaD,l,T)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'$F_D=0.1,\Omega_D=1$')
d=DampedDriven(0,0.2,1,0.5,1,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'$F_D=0.5,\Omega_D=1$')
d=DampedDriven(0,0.2,1,0.99,1,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'$F_D=0.99,\Omega_D=1$')
d=DampedDriven(0,0.2,1,2,0.1,2,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'$F_D=2.0,\Omega_D=2$')
plt.text(13,-0.35,r'$\theta_0=0.2,q=1,l=1$')
plt.xlim(0,20)
plt.title('Damped Driven Pendulum')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.grid(True,color='k')
plt.legend()
plt.show()

import pylab as pl
import math
class Pendulum :
    def __init__(self,i=0,initial_theta=0.2,time_step=0.04,total_time=200,length=9.8,\
                 g=9.8, initial_omega=0,q=0.5,Fd=1.35,omegaD=0.66667,dF=0.001):
        self.theta=[initial_theta]
        self.theta0=[initial_theta]
        self.t=[0]
        self.omega=[initial_omega]
        self.dt=2*math.pi/1000*omegaD
        self.time=total_time
        self.g=g 
        self.l=length
        self.q=q
        self.Fd=Fd
        self.omegaD=omegaD
        self.a=[0]
        self.b=[0]
        self.Fd=[Fd]
        self.dF=dF
    def run(self):
        while (self.Fd[-1]<=1.5):
            _time=0
            while(_time<self.time):
                self.omega.append(self.omega[-1]-((self.g/self.l)*math.sin(self.theta[-1])+\
                     self.q*self.omega[-1]-self.Fd[-1]*math.sin(self.omegaD*self.t[-1]))*self.dt)            
                self.theta.append(self.theta[-1]+self.omega[-1]*self.dt)
                self.t.append(_time)            
                _time += self.dt
                if(self.theta[-1]>=math.pi):
                    self.theta[-1]=self.theta[-1]-2*math.pi
                if(self.theta[-1]<=-math.pi):
                    self.theta[-1]=self.theta[-1]+2*math.pi 
                if(self.t[-1]%(2*math.pi/self.omegaD)<0.002 and self.t[-1]/(2*math.pi/self.omegaD)>15):
                  #  self.a.append(self.omega[-1])
                    self.b.append(self.theta[-1])
                    self.Fd.append(self.Fd[-1])
            self.Fd[-1]+=self.dF
    def show_results(self):
        pl.plot(self.Fd,self.b,'.',color='black')
        pl.title('Bifurcation diagram')
        pl.xlabel('$F_D$')
        pl.ylabel('theta')
        pl.xlim(1.35,1.5)
        pl.ylim(1,3)
        pl.show()

a = Pendulum()
a.run()
a.show_results()

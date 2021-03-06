import matplotlib.pyplot as plt
import numpy as np
class billiard_ellipse:### x^2/3+y^2/2 = 1
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
  
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (self.x[i]**2/4+self.y[i]**2/3 > 1.0):
                self.x[i],self.y[i] = self.correct('x**2/4+y**2/3 < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect((3./4)*self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y, self.vx       
     
    def plot1(self):
        plt.subplot(1,2,1)
        plt.xlim(-2,2)
        plt.ylim(-2,2)
        plt.xlabel('x')
        plt.ylabel('y')
        self.plot_boundary()
        plt.plot(self.x,self.y,color='blue')
        plt.show()
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt  
    def reflect(self,x,y,vx,vy):
        module = np.sqrt(x**2+y**2)  ### normalization
        x = x/module
        y = y/module
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*y)/v
        cos2 = (vx*y-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*y
        vy_n = vt*y-vc*x
        return vx_n,vy_n
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        while theta < 2*np.pi:
            x.append(np.sqrt(4)*np.cos(theta))
            y.append(np.sqrt(3)*np.sin(theta))
            theta+= 0.01
        plt.title(r'Elliptical stadium  $\frac{x^2}{4}+\frac{y^2}{3} = 1$')
        plt.plot(x,y,color='black')
    def plot2(self):
        for i in range(1000):
            if 1000*i<=len(self.x):
                plt.scatter(self.x,self.vx)
                plt.scatter(0,1,color='black',alpha=1,linewidth=4,label='initial')
                plt.figure
                plt.subplot(1,2,2)
                plt.xlabel("x")
                plt.ylabel("$v_x$")

A=billiard_ellipse(2,0,1,0.5,11000,0.01)
A.motion_calculate()
A.plot1()
B=billiard_ellipse(2,0,1,0.5,11000,0.01)
B.motion_calculate()
B.plot2()

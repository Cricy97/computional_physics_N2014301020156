import matplotlib.pyplot as plt
import math


vy0=1.5


GM=4*math.pi*math.pi

class orbit:
    def __init__(self):
        self.x21=[1]
        self.y21=[0]
        self.x22=[1]
        self.y22=[0]
        self.x23=[1]
        self.y23=[0]
        self.x24=[1]
        self.y24=[0]
        self.vx1=[0]
        self.vy1=[0]
        self.vx2=[0]
        self.vy2=[vy0*math.pi]
        self.t=[0]
        self.dt=0.002
        self.x1=[0]
        self.y1=[0]
        

    def calculate1(self):
        while self.t[-1]<10:

            r=math.sqrt((self.x1[-1]-self.x21[-1])**2+(self.y1[-1]-self.y21[-1])**2)
            ox21=-GM*(self.x21[-1]-self.x1[-1])/(r**3.01)
            oy21=-GM*(self.y21[-1]-self.y1[-1])/(r**3.01)
            self.vx2.append(self.vx2[-1]+ox21*self.dt)
            self.vy2.append(self.vy2[-1]+oy21*self.dt)
            self.x21.append(self.x21[-1]+self.vx2[-1]*self.dt) 
            self.y21.append(self.y21[-1]+self.vy2[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        
        return self.x21,self.y21
        
    def calculate2(self):
         while self.t[-1]<5:

            r=math.sqrt((self.x1[-1]-self.x22[-1])**2+(self.y1[-1]-self.y22[-1])**2)
            ox22=-GM*(self.x22[-1]-self.x1[-1])/(r**3.1)
            oy22=-GM*(self.y22[-1]-self.y1[-1])/(r**3.1)
            self.vx2.append(self.vx2[-1]+ox22*self.dt)
            self.vy2.append(self.vy2[-1]+oy22*self.dt)
            self.x22.append(self.x22[-1]+self.vx2[-1]*self.dt) 
            self.y22.append(self.y22[-1]+self.vy2[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        
         return self.x22,self.y22
        
    def calculate3(self):
         while self.t[-1]<4:

            r=math.sqrt((self.x1[-1]-self.x23[-1])**2+(self.y1[-1]-self.y23[-1])**2)
            ox2=-GM*(self.x23[-1]-self.x1[-1])/(r**3.5)
            oy2=-GM*(self.y23[-1]-self.y1[-1])/(r**3.5)
            self.vx2.append(self.vx2[-1]+ox2*self.dt)
            self.vy2.append(self.vy2[-1]+oy2*self.dt)
            self.x23.append(self.x23[-1]+self.vx2[-1]*self.dt) 
            self.y23.append(self.y23[-1]+self.vy2[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        
         return self.x23,self.y23
        
    def calculate4(self):
         while self.t[-1]<1:

            r=math.sqrt((self.x1[-1]-self.x24[-1])**2+(self.y1[-1]-self.y24[-1])**2)
            ox2=-GM*(self.x24[-1]-self.x1[-1])/(r**4)
            oy2=-GM*(self.y24[-1]-self.y1[-1])/(r**4)
            self.vx2.append(self.vx2[-1]+ox2*self.dt)
            self.vy2.append(self.vy2[-1]+oy2*self.dt)
            self.x24.append(self.x24[-1]+self.vx2[-1]*self.dt) 
            self.y24.append(self.y24[-1]+self.vy2[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        
         return self.x24,self.y24




    def show1(self):
    
        plt.subplot(221)
        plt.scatter(self.x1,self.y1,label='sun')
        plt.scatter(self.x21,self.y21,label='planet beta=2',s=0.1,color='black')
        plt.xlabel('x(AU)')
        plt.ylabel('y(AU)')
        plt.title('beta=2.01')
        plt.xlim(-1.2,1.2)
        plt.ylim(-1,1)
        
    def show2(self):
        
        plt.subplot(222)
        plt.scatter(self.x1,self.y1,label='sun')
        plt.scatter(self.x22,self.y22,label='planet beta=2.01',s=0.1,color='black')
        plt.xlabel('x(AU)')
        plt.ylabel('y(AU)')
        plt.title('beta=2.1')
        plt.xlim(-1.2,1.2)
        plt.ylim(-1,1)
        
    def show3(self):
        
        plt.subplot(223)
        plt.scatter(self.x1,self.y1,label='sun')
        plt.scatter(self.x23,self.y23,label='planet beta=2.5',s=0.1,color='black')
        plt.xlabel('x(AU)')
        plt.ylabel('y(AU)')
        plt.title('beta=2.5')
        plt.xlim(-1.2,1.2)
        plt.ylim(-1,1)
        
    def show4(self):
        
        plt.subplot(224)
        plt.scatter(self.x1,self.y1,label='sun')
        plt.scatter(self.x24,self.y24,label='planet beta=3',s=0.1,color='black')
        plt.xlabel('x(AU)')
        plt.ylabel('y(AU)')
        plt.title('beta=3')
        plt.xlim(-1.2,1.2)
        plt.ylim(-1,1)



        plt.show()

a=orbit()
a.calculate1()
a.show1()
b=orbit()
b.calculate2()
b.show2()
c=orbit()
c.calculate3()
c.show3()
d=orbit()
d.calculate4()
d.show4()

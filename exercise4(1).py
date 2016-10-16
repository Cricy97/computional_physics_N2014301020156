import pylab as py
import math

g = 9.8
b2m = 1e-5

class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        next_t = current_state.t + self.dt

    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0

    def show_trajectory(self):
        global x,y        
        x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)

a = cannon(flight_state(0, 0, 700*cos(pi*30/180), 700*sin(pi*30/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'r',label = r'$\theta=30^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
a_final = x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*35/180), 700*sin(pi*35/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'b',label=r'$\theta=35^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*40/180), 700*sin(pi*40/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'y',label=r'$\theta=40^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'c',label=r'$\theta=45^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*50/180), 700*sin(pi*50/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'g',label=r'$\theta=50^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*55/180), 700*sin(pi*55/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,color='m',label=r'$\theta=55^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

title('trajectory of cannon shell')
xlabel('x(km)')
ylabel('y(km)')
show()

import math
from pylab import *

theta_1 = []
omega_1 = []
t_1 = []
v_x_1 = []
v_y_1 = []
x1 = []
y1 = []
theta_1.append(0)
omega_1.append(0)
t_1.append(0)
v_x_1.append(0)
v_min = 2* math.pi
v_y_1.append(v_min)
dt = 0.0001
x1.append(1.0)
y1.append(0)
for i in range(int(100000)):
	tmp1 = omega_1[i]-dt*3*12*math.pi*(x1[i]*math.sin(theta_1[i])-y1[i]*math.cos(theta_1[i]))*(x1[i]*math.cos(theta_1[i])+y1[i]*math.sin(theta_1[i]))/((x1[i]**2+y1[i]**2)**0.5**5)
	omega_1.append(tmp1)
	tmp2 = theta_1[i]+omega_1[i+1]*dt
	while abs(tmp2)>math.pi:
		if tmp2>math.pi:
			tmp2 = tmp2 - 2*math.pi
		else:
			tmp2 = tmp2 + 2*math.pi
	theta_1.append(tmp2)
	tmp3 = v_x_1[i]-4*math.pi**2*x1[i]*dt/((x1[i]**2+y1[i]**2)**0.5**3)
	v_x_1.append(tmp3)
	tmp4 = x1[i]+v_x_1[i+1]*dt
	tmp5 = v_y_1[i]-4*math.pi**2*y1[i]*dt/((x1[i]**2+y1[i]**2)**0.5**3)
	v_y_1.append(tmp5)
	tmp6 = y1[i]+v_y_1[i+1]*dt
	x1.append(tmp4)
	y1.append(tmp6)
	tmp7 = t_1[i] + dt
	t_1.append(tmp7)
print len(t_1)
print len(theta_1)


subplot(121)
title('theta versus time')
xlim(0,8)
ylim(-4,4)
ylabel('theta(radians)')
xlabel('time')
plot(t_1,theta_1,c='blue')
subplot(122)
title('omega versus time')
xlim(0,8)
ylim(0,15)
ylabel('omega(radians)')
xlabel('time')
plot(t_1,omega_1,c='blue')

show()

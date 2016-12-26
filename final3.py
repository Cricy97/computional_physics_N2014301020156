from __future__ import division
import numpy as np
from copy import deepcopy
from cmath import *
import matplotlib.pyplot as plt

dx=0.0065
T=149


class power:
    
    def iteration(self):
        self.x = np.linspace(0,0.65,101)
        self.y_now = np.zeros(101)
        for i in range(101):
            if i<=10:
                self.y_now[i] = (1/20000)*i
            else:
                self.y_now[i] = -(1/180000)*i + 5/9000
        self.y_now[0] = 0
        self.y_now[-1] = 0
        self.y_before = deepcopy(self.y_now)
        self.y_after = np.zeros(101)
        self.disp = [self.y_now[5]]
        for j in range(999):

            for i in range(101):
                if i== 0 or i== 100:
                    self.y_after[i] = 0
                else:
                    self.y_after[i] = - self.y_before[i] + self.y_now[i+1] + self.y_now[i-1]
 
            self.y_before = deepcopy(self.y_now)
            self.y_now = deepcopy(self.y_after)
            self.bridgeforce.append(T*(self.y_now[1]-self.y_now[0])/dx)
        return self.bridgeforce
    def frequency(self):
        self.bridgeforce_fft = np.fft.fft(self.bridgeforce)
        self.bridgeforce_power = []
        self.frequency = []
        for i in range(1000):
            if i==0:
                self.bridgeforce_power.append(abs(self.bridgeforce_fft[i]))
                f = 0
                self.frequency.append(f)
            else:
                self.bridgeforce_power.append(abs(self.bridgeforce_fft[i]))
                T = 10.24/(320*i)
                f = 1/T
                self.frequency.append(f)




A=power(0)
A.iteration()
A.frequency()
plt.plot(A.frequency, A.bridgeforce_power,'k')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Bridge Power(arbitrary units)')
plt.title('Guitar spectrum:pluck at 1/10')
plt.xlim(0,5000)
plt.show()

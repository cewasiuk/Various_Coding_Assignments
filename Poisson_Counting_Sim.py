#! /usr/bin/env python3
#
#Counting Simulation
#
#1June2020
import numpy as np 
import math as ma
import scipy
from scipy.special import factorial
import matplotlib.pyplot as plt 
from time import sleep
#Part (a)
def sim():
    n = np.random.randint(0,1000,1000)
    ye, no = 0, 0
    for i in range(1000):
#        sleep(0.001) #allows sleep between each interval for 1 millisecond, removed bc its likely unwanted and just slows down the prog
        if n[i] >= 2:
            no += 1
        else:
            ye += 1 
    return ye
a = sim()
print(a)

#Part (b)
b = np.zeros(1000)
for j in range(1000):
    b[j] = sim()
x = np.arange(0, int(max(b)), 0.1)
mu = np.average(b)
sig = ma.sqrt(mu)
poisson = 1000*((1/factorial(x))*(mu**x)*np.exp(-mu))

f1, ax1 = plt.subplots()
ax1.hist(b, int(max(b)), edgecolor='grey', color='red')
ax1.plot(x, poisson, color='blue')
ax1.set_title('Average Photon Detection for 1000 Trials')
ax1.set_xlabel('Photon Detections (N)')
ax1.set_ylabel('Probability')
f1.show()

input('\nPress <Enter> to exit...>\n')



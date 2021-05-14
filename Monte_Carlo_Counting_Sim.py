#! /usr/bin/env python3 
#
#Monte Carlo Circle
#
#26May2020
import math as ma
import numpy as np
import matplotlib.pyplot as plt 
#both parts (a) and (b) incorporated

#(a) Monte Carlo Prog
n = input('Please input the number of random points within the circle: ')
N = int(n)
center = 0
j = []
l = []

for i in range(1,N+1):
    #returns number in rand [0.0,1.0)
    x = 2.0 * np.random.random()
    y = 2.0 * np.random.random()
    rad = ma.sqrt((x - 1) ** 2  + (y - 1) ** 2)
    if rad <= 1:
        center += 1
    pimonte = (4 * center / i )
    sigma = (ma.pi - pimonte)/ ma.pi
    j.append(i)
    l.append(abs(sigma))
print('The estimate for pi is: ')
print(pimonte)

xval = 2 * np.random.random(N)
yval = 2 * np.random.random(N)
f1, ax1 = plt.subplots()
circ = plt.Circle((1,1), 1 ,color='r')
ax1.add_artist(circ)
ax1.plot(xval , yval, '.')
ax1.set_xlim(0,2)
ax1.set_ylim(0,2)
ax1.set_title('Monte Carlo Circle for Estimating Pi')
f1.show()

#(b) Fractional Err Plot
f2, ax2 = plt.subplots()
ax2.plot(j,l)
ax2.set_xlabel('Number of Points')
ax2.set_ylabel('Error due to Increasing Number of Points')
ax2.set_title('Fractional Error in Pi using the Monte Carlo Method')
f2.show()

input('Press <Enter> to exit...')



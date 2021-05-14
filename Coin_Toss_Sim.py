#! /usr/bin/env python3
#
#Coin Toss Sim
#
#1 June 2020
import math as ma
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

#Part (a)
def toss():
    n = np.random.randint(0,2,100) #upper bound exclusive
    h, t = 0, 0 
    for i in range(100):
        if n[i] == 0:
            h += 1
        else:
            t += 1
    return h

a = toss()
print('The number of heads out of 100 random coin flips are: ')
print(a)

#Part (b)
l = np.zeros(1000)
for j in range(1000):
    l[j] = toss()

f1, ax1 = plt.subplots()
plt.hist(l, bins=30, edgecolor='grey', linewidth='1', density=True, color='red')
plt.title('Probability of Flipping Heads')
ax1.set_xlabel('Number of Flips out of 100')
ax1.set_ylabel('Number of Heads')

#Part (c)
mean, std = norm.fit(l)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
y = norm.pdf(x, mean, std)
plt.plot(x, y, linewidth=2, color='blue')
f1.show()

input('\nPress <Enter> to exit...>\n')


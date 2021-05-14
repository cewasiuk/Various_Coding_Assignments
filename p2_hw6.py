#! /usr/bin/env python3
#
#Plotting Trig Functions
#
#8May2020

import math as ma
import numpy as np
import matplotlib.pyplot as plt


theta=[]
s=[]
c=[]
for i in range(0,1570):
	a = ma.sin(i/100)
	b = ma.cos(i/100)
	t = i/100
	theta.append(t)
	s.append(a)
	c.append(b)

plt.plot(theta,s,'r.')
plt.plot(theta,c,'b-')
plt.ylabel('Amplitude')
plt.xlabel('Theta')
plt.title('Trig Functions vs Theta')
plt.show()

input("\nPress <Enter> to exit...\n")

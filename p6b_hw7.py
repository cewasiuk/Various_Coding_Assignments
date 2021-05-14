#! /usr/bin/env python3
#
#Heat Transfer (b)
#
#17May2020
import matplotlib.pyplot as plt
import numpy as np 
import math as ma

data = np.loadtxt('p6_data.txt', delimiter='\n')
l=[]
exp=[]
for i in range(len(data)):
	l.append(i)
	exp.append(17.358*ma.exp(0.00061*i))

print(data)

plt.plot(l,data, label='Heat Data')
plt.plot(l,exp,label='Exponential Fit')
plt.legend()
plt.title('Heat Transfer Data as an Exponential')
plt.xlabel('Data Samples (n)')
plt.ylabel('Temperature (C)')
plt.show()
#The time constant when the exponent is 1/e is -6318.12. This exponential would not necessarily have a real time constant since it is exponential growth, not decay.
input("\nPress <Enter> to exit...\n")

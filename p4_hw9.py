#! /usr/bin/env python3 
#
#Numerical Integration 
#
#2June2020
import matplotlib.pyplot as plt 
import numpy as np
import math as ma 
from random import random 

#Part (a)
def gaussian(x):
    return np.exp(-(x**2))
x1 = -25 #Gaussian function tends to zero at infinity, this is a decent approximation for upper and lower limits of summation
x2 = 25
n = 50
dx = (x2-x1)/n #essentially allows for a reimmann summation for rectangles of width 1. 
summation = 0

for i in range(x1, int(x2 - dx)):
    summation = summation + gaussian(i) #allows for a sum over all rectangles of width 1 and height y = exp(-x**2)
rounded = round(summation, 4)
print('The value of a Reimann sum of a Gaussian Function (with amplitude 1) from negative infinity to infinity is approximately :',rounded)

#Producing the error compared to the actual known value
realv = np.sqrt(np.pi)
error1 = np.zeros(50)
reimann = 0
for j in range(n):
    reimann = gaussian(j) * dx 
    error1[j] = np.sum(reimann)
error1 = error1/realv

#Part(b)
while True:
    a = input('Please input the number of specified points for the Monte Carlo Method of integration: ')
    try:
        b = int(a)
    except ValueError:
        print('Please input an integer')
    else: 
        break

l = []
error2 =[]
point = 0
for k in range(b):
    xval = np.random.randint(-25,25)
    yval = random()
    funct = gaussian(xval)
    if yval <= funct:
        point += 1 
    approx = 50 * (point / b)
 #point/b is percentage of points within function, multiplied by the number of points gives an approx for area underneath the function
    ierr = 50 * (point/(k+1))
    l.append(ierr)
print('The Monte Carlo approximation for the area below a normalized Gaussian is ', approx)

for i in l:
    e = abs((np.sqrt(np.pi) - i)/np.pi)
    error2.append(e)
    
#Plotting Error Functions
x1 = np.arange(0,50)
f1, ax1 = plt.subplots()
ax1.set_title('Error in Integration of a Normalized Gaussian using a Summation of Rectangles')
ax1.set_xlabel('Number of Rectangles')
ax1.set_ylabel('Fractional Error')
ax1.plot(x1, error1)
f1.show()

x2 = np.arange(0,b)
f2, ax2 = plt.subplots()
ax2.set_title('Error in Integrating using the Monte Carlo Method')
ax2.set_xlabel('Number of Random Points')
ax2.set_ylabel('Fractional Error')
ax2.plot(x2, error2)
f2.show()

input('Press <Enter> to exit...')

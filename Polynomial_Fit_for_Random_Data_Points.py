#! /usr/bin/env python3 
#
#Polynomial Fits 
#
#26May2020
import math as ma 
import numpy as np 
import matplotlib.pyplot as plt
#will use the numpy.polyfit function to fit our randomized data points

print('This program will fit polynomials to N random points on a graph')
def fit(xrand, yrand, deg):
    linefit = np.polyfit(xrand, yrand, deg)
    poly = np.poly1d(linefit)
    x = np.linspace(0, 100, 100)
    y = poly(x)
    return y 

while True:
    n = input('Please input an integer less than 20 to specify the number of random points: ')
    try:
        N = int(n)
        if N <= 20 and N > 0:
            break
        else:
            print('Please try again')
    except ValueError: #portion that deals with non-numerical inputs
        print('Please try again')

xrand = np.random.randint(0, 100, N)
yrand = np.random.randint(0, 100, N)
x = np.linspace(0, 100, 100)

f1, ax1 = plt.subplots()
ax1.scatter(xrand, yrand)
ax1.plot(x, fit(xrand, yrand, 1),'r', label='Degree = 1')
ax1.plot(x, fit(xrand, yrand, N-1), 'b', label='Degree = N-1')
ax1.plot(x, fit(xrand, yrand, N-3), 'g', label='Degree = N-3')
ax1.legend()
ax1.set_ylim(-10,110)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Fitting Polynomials to Random Integers')
f1.show()

input('\nPress <Enter> to exit...>\n')




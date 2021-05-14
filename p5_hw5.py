#! /usr/bin/env python3 
#
#Mandelbrot Set
#1May2020
#

import numpy as np
import matplotlib.pyplot as plt
import math
import sys


#Defining our image size and grid scalings
X=512
Y=384

xcen = int(X/2)
ycen = int(Y/2)

xmax=1
xmin=-1
ymax=1
ymin=-1

xsiz = (xmax - xmin)/X
ysiz = (ymax - ymin)/Y
c = complex(-.8,0.17)
#Complex numbers chosen randomly until a part of the Mandelbrot set was produced

#defining our mandelbrot criterion 
def mandelbrot(z):
	value = z**2 + c
	return value


def smalllim(z0):
	Zn = z0
	n = 0
	while n <= 250:
		Zn = mandelbrot(Zn)
#limit defined to be two, since anything greater than 2 will diverge within the set
		if abs(Zn) > 2:
			break
		n += 1
	return n 

#A lot of the plotting lines taken from examples in folder physrpi
colorpxl = np.zeros( (X,Y), dtype='uint8')

#complex number zn chosen to be a combination of the x and y values. 
#Attempted to zoom in using different complex zn values. Original plot in file made using x1/5 and y1/5. Current picture appears more zoomed when dividing by a larger number.

plot = np.zeros( (X,Y) )
for i in range(X):
	for j in range(Y):
#lines below allows the function to be defined within our desired grid
		x1 = (i - xcen)*xsiz
		y1 = (j - ycen)*ysiz
		zn=complex(x1/40,y1/40)
		n=smalllim(zn)
		plot[i,j] = n

colorpxl = plot

plotar = np.flipud(colorpxl.transpose())

#colormap 'viridis' chosen bc it looked cool
f1, ax1 = plt.subplots()
mand = ax1.imshow(plotar, interpolation='none', cmap= 'viridis')
ax1.axis('off')

f1.show()
input('press <Enter> to exit')

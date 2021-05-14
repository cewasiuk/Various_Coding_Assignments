#! /usr/bin/env python3 
#
#P3 - Surface Plot 
#
#9May2020

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

splot = plt.figure()
three = splot.gca(projection='3d')

#defining inputs 
x = np.arange(0,5*np.pi,0.2)
y = np.arange(0,5*np.pi,0.2) 
#5pi = 2.5 Periods with 0.2 steps

#returns coordinate matricies
[x, y] = np.meshgrid(x, y)
s = np.sin(x)
c = np.cos(y)
#defining a function for z(x,y)
def z():
    prod = (s*c)
    return prod


surface = three.plot_surface(x, y, z(), cmap=cm.twilight,linewidth=0, antialiased=False)
#defining z-axis
three.set_zlim(-2.00, 2.00, 0.2)
three.zaxis.set_major_locator(LinearLocator(10))
three.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

splot.colorbar(surface, shrink=0.5, aspect=5)
plt.show()

input("\nPress <Enter> to exit...\n")

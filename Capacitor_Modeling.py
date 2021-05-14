#! /usr/bin/env python3 
#
#Capacitor Potential Relaxation
#
#9June2020
import numpy as np 
import time
import matplotlib.pyplot as plt

#specifications for variables (as functions of the grid)
it = 2000
grid = 100
cpthick = 8/grid
cpwidth = 8/grid
gap = 0/grid
pot = 40

#Want to specify the potential on the bounds of each capacitor 
def capacitor_bounds(a):
    xleft = int(0.5 * grid * (1 - cpwidth))
    xright = int(0.5 * grid * (1 + cpwidth))
    ydn1 = int(grid * (0.5  - cpthick - 0.5 * gap)) #Capacitor 1 = -Vlt
    yup1 = int(ydn1 + cpthick * grid)
    ydn2 = int(yup1 + gap * grid) #Capacitor 2 = +Vlt
    yup2 = int(ydn2 + cpthick * grid)

    a[xleft:xright, ydn1:yup1] = -pot
    a[xleft:xright, ydn2:yup2] = pot

    a[:,0] = 0.0
    a[0,:] = 0.0
    a[-1,:] = 0.0
    a[:,-1] = 0.0

init = np.zeros((grid,grid), dtype='float')
b = np.zeros((grid,grid), dtype='float')

capacitor_bounds(init)
t0 = time.perf_counter()

#used code seen in the lecture  
for k in range(it):
    b  = (np.roll(init,1,0)+np.roll(init,-1,0)+np.roll(init,1,1)+np.roll(init,-1,1))/4
    capacitor_bounds(b)
    init = np.copy(b)
tf = time.perf_counter() - t0


plot = np.flipud(init.transpose())
f1, ax1 = plt.subplots()
img = ax1.imshow(plot, interpolation='none', cmap='twilight')
#turning off axis labels for plot
ax1.axis('off')
f1.show()

input("\nPress <Enter> to exit...\n")    


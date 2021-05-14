#! /usr/bin/env python3
#
#3-4-5- Triangle
#1May2020

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

#This portion changes the size of the desired image
X = 512
Y = 600

#Defined in img.py
pvals = np.zeros((X,Y,3), dtype='uint8')
pvals[:,:,:] =0xff


#Loop used for the hypotenuse of the triangle, which sets a bunch of vertical stripes for some y values. Coefficients found by trial and error.
for i in range(0,320):
   hype = int((4/3)*i)
   pvals[int(hype-15):int(hype+15),95 + i,:] = (0,0,0xff)


#Again stolen from img.py
plotarr = np.flipud(pvals.transpose(1,0,2))

f1, ax1 = plt.subplots()
ax1.axis('off')

picture = ax1.imshow(plotarr, interpolation='none')
f1.show()
f1.canvas.draw()

#The first two lines below correspond to the specific legs of the triangle (4 and 3 respectively) and sisimply run from according to specified pixel lengths. The width for both sections runs 20 pixels wide, and the lengths are found according to relative distance to ensure a 3-4-5 triangle. 

#The bottom two lines are used as correction terms since the hypotenuse runs messier than desired. The correction lines are essentially massive areas set to the color white that overlap the messier parts of the drawing.  

pvals[int(20):int(413),int(107):int(127),:] = (0,0,0xff)  #4
pvals[int(393):int(413),int(107):int(407),:] = (0,0,0xff) #3
pvals[int(413):int(440),int(0):int(600),:] = (0xff, 0xff, 0xff) #correction
pvals[int(0):int(414),int(0):int(107),:] = (0xff, 0xff, 0xff) #correction

picture.set_data(plotarr)
ax1.draw_artist(picture)
f1.canvas.blit(ax1.bbox)

input('\nPress <Enter> to exit...\n')


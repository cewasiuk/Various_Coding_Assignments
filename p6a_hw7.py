#! /usr/bin/env python3
#
#Heat Transfer (a)
#
#17May2020
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
#imported Adafruit from the tempdemo.py
#Placed an ice tray overtop of my sensor and then let the cool air fall and reduce the temp surrounding the sensor
import Adafruit.MCP9808 as MCP9808
sensor = MCP9808()
sensor.begin()

ACQTIME = 20.0 
SPS = 4 

nsamp = int(ACQTIME*SPS)
sint = 1.0/SPS
data = np.zeros(nsamp, 'float')

input('Press <Enter> to start %.1f s data acquisition...' % ACQTIME)
print()

t0 = time.perf_counter()
for i in range(nsamp):
   st = time.perf_counter()
   data[i] = sensor.readTempC()
   while (time.perf_counter() - st) <= sint:
      pass

t = time.perf_counter() - t0
xpoints = np.arange(0, ACQTIME, sint)

print('Time elapsed: %.9f s.' % t)
print()

f1, ax1 = plt.subplots()
ax1.plot(xpoints, data)
#labels
ax1.set_title('Temperature Sensor Response')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Temperature (C)')
#show our figure
f1.show()

l=[]
f = open("p6_data.txt", "w")
for j in range(len(data)):
    l.append(float(data[j]))
for k in range(len(l)):
    f.write(str(l[k]))
    f.write('\n')

input("\nPress <Enter> to exit...\n")



#! /usr/bin/env python3
#
#Acquire and Store Data
#
#15May2020
#copied code from adcdemo.py and stripchart.py

ACQTIME = 1.0
SPS = 920
VRANGE = 4096
nsamples = int(ACQTIME*SPS)
sinterval = 1.0/SPS

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import os
from Adafruit import ADS1x15
###############################################################################

indata = np.zeros(nsamples,'float')

print()
print('Initializing ADC...')
print()
adc = ADS1x15()
adc.startContinuousDifferentialConversion(2, 3, pga=VRANGE, sps=SPS)

input('Press <Enter> to start %.1f s data acquisition...' % ACQTIME)
print()

t0 = time.perf_counter()

for i in range(nsamples):
   st = time.perf_counter()
   indata[i] = 0.001*adc.getLastConversionResults()
   while (time.perf_counter() - st) <= sinterval:
      pass

t = time.perf_counter() - t0

adc.stopContinuousConversion()

xpoints = np.arange(0, ACQTIME, sinterval)

print('Time elapsed: %.9f s.' % t)
print()

f1, ax1 = plt.subplots()
ax1.plot(xpoints, indata)
ax1.set_title('Voltage Sample for 1s')
ax1.set_xlabel('Time(s)')
ax1.set_ylabel('Voltage (V)')
f1.show()
input("\nPress <Enter> to exit...\n")

#copied from p4_hw7.py
f = open("p5_data.txt", "w")
l=[]
for j in range(len(indata)):
    l.append(float(indata[j]))
for k in range(len(l)):
    f.write(str(l[k]))
    f.write('\n')


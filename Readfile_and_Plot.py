#!/usr/bin/env python3


#
#Wind Speed
#
#30Apr20
#
import sys
import os 


wind = open('wind.dat', 'r')
read_wind = wind.readlines()


time = []
wind = []
err = []
for i in range(len(read_wind)):
	stripped = read_wind[i].rstrip('\n')
	split = stripped.split(' ')
	a=float(split[0])
	b=float(split[1])
	c=float(split[2])
	time.append(a)
	wind.append(b)
	err.append(c)


import numpy as np
import matplotlib.pyplot as plt

plt.errorbar(time,wind,yerr=err, fmt='b.',capsize=3)
plt.xlabel('Time (hours)')
plt.ylabel('Avg Wind Speed (knots)')
plt.title('Wind Speed vs Time of Day')

plt.show()

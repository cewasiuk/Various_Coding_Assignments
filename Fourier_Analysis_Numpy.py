#! /usr/bin/env python3 
#
#Fourier Analysis
#
#17May2020
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import psd

data = np.loadtxt('p5_data.txt', delimiter='\n')
samples = 920
t = np.linspace(0,1,samples)
offset= data - np.mean(data)

#Creates two separate plots, one for orginal data, one for the power spectrum
f1, ax1 = plt.subplots()
ax1.plot(t,offset)
ax1.set_title('Voltage of Strobelight over Timescale of 1 second')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)')
f1.show()

y, x = psd(offset, NFFT=samples, Fs=samples, pad_to=16*samples)
f2, ax2 = plt.subplots()
ax2.plot(x,y)
ax2.set_xlim(0,15)
ax2.set_title('FT of P5_Data')
ax2.set_xlabel('Fundamental Frequency (Hz)')
ax2.set_ylabel('Power (W)')
f2.show()


input("\nPress <Enter> to exit...\n")
print('The fundamental frequency is 12 Hz')

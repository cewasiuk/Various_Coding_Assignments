#!/usr/bin/env python3
 
#Part (a)
#Read Temp File by running cat 
#
# 20April20
#

import subprocess 
import os 
import math 
import time 

def repeat(arg):
	time.sleep(1)
	print(arg)

print()
i=0
while i < 1000000:

	os.chdir("/sys/class/thermal/thermal_zone0")

	ret1=  subprocess.check_output('cat temp', shell=True)

	temp = int(ret1)/1000
 
	print("Timer (s):", i)
	repeat(temp)
	i += 1

#When the infinite loop is run, the internal temperature of the processor is increased dramatically. In my case, the temp jumped nearly 10 degrees in about fifteen seconds.

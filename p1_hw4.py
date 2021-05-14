#!/usr/bin/env python3

#
#Prompt for an integer, return a string. Continue prompting if recieved an error. Print out prime factors of variable input
#
#
#

import math as ma

#Tried running but recursion took too much computing time for such large numbers
#def factorial(n):
#	if n == 0:
#		return 1
#	if n==1:
#		return n
#	else:
#		return n*factorial(n-1)

while True:
	instr = input("Please enter an integer: ")
	try:
		val = int(instr)
	except ValueError:
		print("Your input was not an integer.  Try again.\n")
	else:
		break
if val < 0:
	print('ooh ur bad')
if (val%2) == 0:
	print(2)

for i in range(3, 2*int(ma.sqrt(abs(val)))):
	if (val%i) == 0 and ((ma.factorial(i-1)+1)%i) == 0:
		print(i)

#! /usr/bin/env python3

#
#Sine Function
#
#25April20

import math as math

pi = 3.14159265

def factorial(num):
	a = 1
	for i in range(num):
		a*=(num-i)
	return a
 
def sind(angle, terms):
    sol = 0
    for j in range(terms+1):
        ft = factorial(2*j + 1)
        sol +=(((-1)**j)/ft) * (angle**(2*j +1))
    return sol

def compare(angle, sol):
	print()
	print('sind() returned the value: ' + str(sol))
	print()
	print('math.sin() returned the value: ' + str(math.sin(angle)))
	print()
	print('The ratio of sind() to math.sin() is: ' +str((sol / math.sin(angle))))
	print()
	print('The absolute difference of the values is: ' +str(abs(sol - (math.sin(angle)))))
	print()

#def comp():
    #theangle = 90
    #rterms = 10

b = True
while(b):
	theangle = input('Please enter angle: ')
	angle = int(theangle)
	if angle !=0:
		b = False
	if angle > 360:
		b = False
h = True
while(h):
	rterms= input('Enter number of terms that is less than 25 which you would like sum in the sine series: ')
	terms= int(rterms)
	if terms <= 25:
		h = False

radians = (angle * pi)/180
    
solution = sind(radians, terms)
compare(radians, solution)


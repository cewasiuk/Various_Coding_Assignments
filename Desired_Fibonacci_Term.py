#! /usr/bin/env python3
 
#Apr27/2019
#Problem 5

def fibnum(num):
    c0, c1 = 1, 1
    for i in range(num):
        yield c0
        c0, c1 = c1, c0 + c1


b = input('Please enter the number of desired Fibonacci terms: ')
d = int(b)
fibfailsafe = fibnum(359)
newfibnum = list(fibnum(d))

#stops sequence at the term that delivers the 75th character of a single string in the fibonacci sequence 
if d > 359:
	for j in fibfailsafe:
		print(j)

#prints the normal string of desired numbers
else:
	for i in newfibnum:
		print(i)



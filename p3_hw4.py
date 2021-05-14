#!/usr/bin/env python3


#
#Execution Speed
#
#25April20
#t0 = used to reset t0 after every step

import time
print()
#(a)
t0 = time.perf_counter()
for i in range (1000000):
    pass
tf = time.perf_counter()

print("The execution time for a pass statement: " )
print((tf-t0)/(1000000))
print()

#(b)
t0 = time.perf_counter()
for i in range(1000000):
	1000+420
tf = time.perf_counter()

print("Execution time for addition of two float point variables: ")
print((tf-t0)/(1000000))
print()

#c
t0 = time.perf_counter()
for i in range (1000000):
    7.10*69.4
tf = time.perf_counter()

print("Execution time for multiplication of two float point variables: ")
print((tf-t0)/1000000)
print()

#d
t0 = time.perf_counter()
for i in range (1000000):
    (90.32)/(23.4)
tf = time.perf_counter()

print("Execution time for division of two float point variables: ")
print((tf-t0)/(1000000))
print()

#(e)
t0 = time.perf_counter()
var1=49
var2=48
for i in range (1000000):
    (var1/var2)
tf= time.perf_counter()

print("Execution time for division of two integer variables: ")
print((tf-t0)/1000000)
print()

#(f)
aaa = [0,50000]
aaa = list(aaa)

t0 = time.perf_counter()
for i in range (1000000):
    aaa.append(5)
tf = time.perf_counter()

print("Execution time for appending one number to a list: ")
print((tf-t0)/(1000000))
print()

#If we change the length of the list the execution time does not change. I checked this by changing the length of the list from 1000 to 50000, ran the program and compared times.

#(g)
def crackhead():
    pass

t0 = time.perf_counter()
for i in range (1000000):
    crackhead
tf= time.perf_counter()

print("Execution time for calling a function that contains a pass statement: ")
print((tf-t0)/1000000)
print()

#(h)
def zooted():
    (69.5)+(22.4)

t0 = time.perf_counter()
for i in range (1000000):
      zooted
tf= time.perf_counter()

print("Execution time for calling a function that adds two float variables: ")
print((tf-t0)/1000000)
print()

#!/usr/bin/env python3

#
#String Processing
# 
# 19April20
#
#
import math 

def word_count(string):
	a = len(string.split())
	return int(a)
#Part (a)
string=input("Please enter a string of at least three words: ") 

#part (b)
while True:
	if word_count(string) > 2:
		break 
	string = input("Please try again: ")

list=string.split()

print( ) #tried multiple line spacing options, this worked the best   

#Part (c)
for i in list:
	print(i)
print( ) 

#Part (d)
string1=string.replace(' ','')
print(string1[0:3])
print( ) 

#Part (e)
print(string1[-3:])
print( ) 

#Part (f) 
print(string[0:int(len(string)/2)])
print( )

#Part (g)
print(string[-int(len(string)/2):])
print( )

#Part (h)
rev= string[::-1]
print(rev)
print( )

#Part (i)
alph=sorted(string1)
print(''.join(alph)) 
print( )

#Part (j)
for i in string1:
	print(i[0])
print( )

#Part (k)
for i in string1:
    print(ord(i[0]))


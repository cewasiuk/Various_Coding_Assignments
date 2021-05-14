#!/usr/bin/env python3


#
# Read File and Average: Read numbers from a designated file, print average
# Used file name 'Readfile' as my test file
# 19April20
#

import math 

def file_readlines(filename):
	infile = open(filename, 'r')
	inlines = infile.readlines()
	infile.close()
	return(inlines)

def average(nums):
	sum=0
	for j in nums:
		sum= sum + j
	avg= sum / len(nums)
	return avg

name = input("Input name of file that user would like to find average:")

lines = file_readlines(name)
list = [] 

for i in lines: 
	list.append(float(i))
print("The average of the numbers defined in ",name, " is: ")
print("%.2f" % average(list))


 
	





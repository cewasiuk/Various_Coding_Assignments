#!/usr/bin/env python3

#
#Valentines Day
#
# 20April20
#
import os 
import csv 
import fileinput

os.chdir("/home/pi/physrpi/coursefiles")

with open('classlist.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	for row in readcsv:
		FIRST = row[1]
		first=FIRST.title()
		LAST= row[0]
		last=LAST.title()
		print("Happy Valentine's Day,", first , last,"!")

 


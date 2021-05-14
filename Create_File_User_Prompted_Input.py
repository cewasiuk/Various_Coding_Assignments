#!/usr/bin/env python3

#
# Write File - Create a file with 2 user provided strings
#
# 19April20
#
import os
import sys

def careful_write(filename):
	if os.access(filename, os.F_OK):
		print('\nOutput file already exists: %s\n\n' % filename, file=sys.stderr)
		quit()
	return
filename=input("Please create a name for the new file:")

careful_write(filename)

line1=input("Please input the first string:")
line2=input("Please input the second string:")

outlines = [line1, line2]

outfile = open(filename, 'w')
for i in outlines:
	outfile.write(i)
	outfile.write('\n')
outfile.close()

#! /usr/bin/env python3
#
#Petal Problem
#3May2020
#
import math as ma

#determines number of petals and also allows a catch for ValueErrors
while True:
	prompt=input('Please choose the number of petals (less than 15) for the flower: ')
	try:
		num=int(prompt)
		if num <= 15 and num > 0:
			break
		else:
			print("invalid number of petals")
	except ValueError:
		print('Invalid Input')
pet = 360/(num+1)
a = ma.exp(num*ma.log(1/3)/10-4*ma.log(1/3)/10)


#copied from petal.ps file
petal = """
 /petal 
   {
   /petalcol [ 0 0 0.8 ] def
   /ep1 [ 0 0 ] def
   /ep2 [ 0 110 ] def
   /cp1 [ 55 75 ] def
   /cp2 [ 10 85 ] def
   /ap {aload pop} def
   gsave
   petalcol ap setrgbcolor
   0 setlinewidth
   rotate 
   scale 

   ep1 ap moveto
   cp1 ap cp2 ap ep2 ap curveto
   cp2 ap exch neg exch
   cp1 ap exch neg exch
   ep1 ap curveto closepath fill

   grestore
   } def

gsave
"""
#derived mainly from lecture
stem = """
/ap {aload pop} def
gsave 
	306 500 translate 
	[0 1 0] ap setrgbcolor
	8 setlinewidth

	[0 0] ap moveto
	[-10 -100] ap lineto 
	[5 -200] ap lineto
	[0 -250] ap lineto 
	[0 -310] ap lineto stroke

grestore
"""
leaves = """
/leaves
	{
	/ep1 [0 0] def
	/ep2 [0 100] def
	/cp1 [55 65] def
	/cp2 [10 95] def	
	/ap {aload pop} def
	gsave
	[0 5 0] ap setrgbcolor
	0 setlinewidth
	rotate
	scale
	
	ep1 ap moveto
	cp1 ap cp2 ap ep2 ap curveto
	cp2 ap exch neg exch
	cp1 ap exch neg exch
	ep1 ap curveto closepath fill

	grestore
	} def

gsave
	296 400 translate
	
	0.8 1 90 leaves
	15 -100 translate
	0.8 0.6 270 leaves

grestore 
"""
#an artist needs to sign his work 
sig= """
	/Helvetica-Bold 20 selectfont

	450  100 moveto 
	(-Christopher) show
	460  70 moveto
	(Ewasiuk) show 

grestore
"""

#creates a postscript file and writes the above functions based on the users input 
flower = open('Flower.ps', 'w+')
flower.write(petal)
flower.write(sig)
flower.write(leaves)
flower.write(stem)
flower.write(" 306 500 translate \n")
#allows for users number to determine the number and spacing of petals
for i in range(num):
	flower.write("   "+str(a)+ " 1 " +str((180+(1+i)*pet)%360)+" petal\n")
flower.write("grestore\n")
flower.close

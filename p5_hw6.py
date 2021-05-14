#! /usr/bin/env python3
#
#Get Web Page with Socket
#
#9May2020

import sys
import os
import socket
from bs4 import BeautifulSoup

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname('web.physics.ucsb.edu')
sockcom = b'GET /~phys129/lipman/ HTTP/1.0\r\n\r\n'

#didnt use bc it didnt end up working, ended up having to look up BeautifulSoup.

def rem_ascii(text):
	return ''.join(i for i in text if ord(i)<128)

#failsafes for if the connection fails
def open_connection():
	try:
		s
	except socket.error:
		print('Could not create socket')
		sys.exit()

def get_host():
	try:
		host
	except socket.gaierror:
		print('Unable to connect to hostname')
		sys.exit()

#Retrieving the course webpage by opening socket to port 80 (http) 
def send():
	s.connect((host,80))
	sockcom
	try:
		s.sendall(sockcom)
#sends data to the socket using the http command 
	except:
		print('Socket could not be sent')
		sys.exit()

open_connection()
get_host()
send()

#defines the number of bytes to be recieved at once, just set to 5000 as a max amount
a = s.recv(5000)
soup = BeautifulSoup(a,'html.parser')
date = soup.find_all('span')[3].contents[0]
print(date)

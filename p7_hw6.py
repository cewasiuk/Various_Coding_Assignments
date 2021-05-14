#! /usr/bin/env python3
#
#Time Server
#
#9May2020

import sys
import os
import socket
import datetime

print('Current time before connecting')
print(datetime.datetime.now())
print()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind(('127.0.0.1', 55555))
s.listen(1)
conn, addr = s.accept()


while True:
	print(datetime.dateteime.now())
	print()
	print('Done.\n')
conn.shutdown(socket.SHUT_RDWR)
conn.close()
#followed many online instructions and was unable to fully connect to the TCP port

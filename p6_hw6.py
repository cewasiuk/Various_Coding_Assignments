#! /usr/bin/env python3
#
#Get Web Page with Requests
#
#9May2020
import requests
from bs4 import BeautifulSoup

#Requests essentially does all of socket's work
req = requests.get('http://web.physics.ucsb.edu/~phys129/lipman/')
#need the correct type to use Beautiful Soup
a = req.content

#Taken from the last problem
soup = BeautifulSoup(a,'html.parser')
date = soup.find_all('span')[3].contents[0]
print(date)


#! /usr/bin/env python3 
#
#fork() and execv()
#
#26May2020
import os 
import time 

#Part (a)
#I used the os.execv command below to use the ls command in the current working directory, which operated as if I were to execute the command within the terminal window. However when I tried to add the print function below it still only executed the ls command, illustrating that the os.execv command killed the python program as well and replaced it with an executable path.

#os.execv('/bin/ls', ['/bin/ls'])
#print('test')

#Part (b)

for i in range(1,10000,1):
    print(i)
    time.sleep(0.5)
    if i % 10 == 0:
        print('Fork Time')
        process = os.fork()
        child = (process == 0)
        if child: 
            for i in range(1,100,1): 
                print('Announcement: About to execute ls -l')
                os.execv('/bin/ls', ['ls', '-l'])


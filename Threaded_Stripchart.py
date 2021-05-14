#! /usr/bin/env python3 
#
#Threaded Stripchart 
#
#26May2020
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import threading

#using prior script
print('An input not within the interval will return the plot to zero.')
class Scope(object):
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = np.array([])
        self.ydata = np.array([])
        self.t0 = time.perf_counter()
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-101, 101) #altered limits
        self.ax.set_xlim(0, self.maxt)

    def update(self, data):
        t,y = data
        self.tdata = np.append(self.tdata, t)
        self.ydata = np.append(self.ydata, y)
        self.ydata = self.ydata[self.tdata > (t-self.maxt)]
        self.tdata = self.tdata[self.tdata > (t-self.maxt)]
        self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
        self.ax.figure.canvas.draw()
        self.line.set_data(self.tdata, self.ydata)
        return self.line,

    def emitter(self, p=0.1):
        global num 
        num = 0
        while True:
            t = time.perf_counter() - self.t0
            try:
                num = float(num)
            except ValueError:
                break            
            if num >=  -100.0 and num <= 100.0:
                yield t, num
            else:
                yield t, 0

#defining an update to the global variable
    def updateval():
        global num 
        while True:
            try:
                num = input('Please input a number in the range [-100,100]: ')
                num = float(num)
            except ValueError:
                print('Wrong input, please try again')
                continue 
        return num

#using code from thread_example.py
if __name__ == '__main__':
    t = threading.Thread(target = Scope.updateval)
    t.start()
    fig, ax1 = plt.subplots()
    scope = Scope(ax1, maxt=10, dt=0.01)
    ani = animation.FuncAnimation(fig, scope.update, scope.emitter, interval=0.01*1000, blit=True)
    plt.show()

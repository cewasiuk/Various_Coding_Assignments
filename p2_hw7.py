#! /usr/bin/env python3
#
#Stripchart
#
#15May2020

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
#copied code from stripchart.py

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
        self.ax.set_ylim(-1.1, 1.1) #altered limits
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

#edited this portion to include the sine function
    def emitter(self, p=0.1):
        while True:
            t = time.perf_counter() - self.t0
            w = np.pi
            s = np.sin((w*t-.5))#added phases so sin(w*t) starts at approximately zero
            if s > p:
                yield t, s
            else:
                yield t, s

if __name__ == '__main__':
    dt = 0.01
    fig, ax = plt.subplots()
    scope = Scope(ax, maxt=10, dt=dt)
    ani = animation.FuncAnimation(fig, scope.update, scope.emitter, interval=dt*1000., blit=True)
    
    ax.set_title('Continuous Sin(wt) vs. Time')
    ax.set_xlabel('Time(s)')
    ax.set_ylabel('Sin(w*t)')
    plt.show()

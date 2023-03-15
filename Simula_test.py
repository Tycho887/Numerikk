# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 22:04:59 2023

@author: Michael
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
import copy
import gc

class Object:
    def __init__(self,mass,position,velocity,name=''):
        self.name = name.strip()
        self.mass = mass
        self.pos = np.array(position,dtype=float)
        self.vel = np.array(velocity,dtype=float)
        self.pos_log = []
        "Position and velocity are 3D vectors"
    def applyForce(self,Force,h):
        "h is the interval step length"
        acc_vector = Force/self.mass
        self.vel += acc_vector*h
        print(acc_vector)
        self.pos += self.vel*h + 0.5*acc_vector*h**2
        self.pos_log.append(copy.deepcopy(self.pos))
    def __str__(self):
        return self.name
    def getPos(self):
        return self.pos_log

def applyForce(obj,dt):
    force = np.array((0,-9.81))*obj.mass
    obj.applyForce(force,dt)

def generate_data(obj,iterations):
    for i in range(iterations):
        applyForce(obj, 0.01)
        
def draw(obj):
    for point in obj.pos_log[::5]:
        x, y = point
        plt.scatter(x,y)
    plt.show()
        
ballast = Object(10, [0.,0.], [25.,25.])
generate_data(ballast, 500)
draw(ballast)
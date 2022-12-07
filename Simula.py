# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:11:55 2022

@author: Michael
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Object:
    def __init__(self,mass,position,velocity,name=''):
        self.name = name.strip()
        self.mass = mass
        self.pos = np.array(position)
        self.vel = np.array(velocity)
        "Position and velocity are 3D vectors"
    def applyForce(self,Force,h):
        "h is the interval step length"
        acc_vector = Force/self.mass
        self.vel += acc_vector*h
        self.pos += self.vel*h + 0.5*acc_vector*h**2
        return self.pos
    def __str__(self):
        return self.name
    def getPos(self):
        return self.pos

Earth = Object(6e24,[1.5e10,3,2],[3e5,100,200])
    
def getObjectsFromFile(file='data/objects.csv'):
    objects = []
    with open(file,'r') as filein:
        for line in filein:
            name,mass,pos,vel = line.split(';')
            mass = float(mass)
            pos = list(map(float, pos.strip().split(',')))
            vel = list(map(float, vel.strip().split(',')))
            objects.append(Object(mass,pos,vel,name=name))
    return objects

def sortObjectsToMass(_objects):
    _objects.sort(key=lambda x: x.mass, reverse=True)

def gravity_equation(_object1,_object2,_distance):
    "Force from object2 on object1"
    "No need to multiply by mass of object 1"
    "This avoids a division operation per cycle"
    G = 6.6743e-11
    #G = 500
    F = (G*_object2.mass)/_distance**2
    
    return F
    

def calculateForceVectors(_objects, force_equation=gravity_equation):
    size = len(_objects)
    Force_matrix = np.ndarray(shape=(len(_objects[0].pos),size,size), dtype=float)
    for i in range(len(Force_matrix[0,])):
        for j in range(i+1,len(Force_matrix[0,])):
            
            vector = _objects[i].pos-_objects[j].pos
            distance = np.linalg.norm(vector)
            unit_vector = vector/distance
            F = force_equation(_objects[i],_objects[j],distance)
            
            Force_matrix[:,i,j]=F*unit_vector;Force_matrix[:,j,i]=-F*unit_vector
    
    return np.sum(Force_matrix, axis=1)

def ApplyForces(_objects):
    forces = calculateForceVectors(_objects)
    for i in range(len(forces[0,])):
        force = forces[:,i]
        _objects[i].applyForce(force,h=10)

def draw_frame(Objects):
    for i in range(len(Objects)):
        print(str(Objects[i]))

        axes = plt.subplot(111, projection='3d')

        x, y, z = Objects[i].pos
        axes.plot(x, y, z, "*", label=f"{Objects[i]}")


        plt.legend(loc="upper right")

    plt.show()


if __name__ == "__main__":
    objects = getObjectsFromFile()
    sortObjectsToMass(objects)
    ApplyForces(objects)
    draw_frame(objects)

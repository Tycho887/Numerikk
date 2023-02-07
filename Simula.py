# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:11:55 2022

@author: Michael
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
#from mpl_toolkits.mplot3d import Axes3D 

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
        self.pos += self.vel*h + 0.5*acc_vector*h**2
        self.vel += acc_vector*h
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
    "This avoids a division operation per iteration"
    G = 6.6743e-11
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
            
            Force_matrix[:,i,j]=F*unit_vector
            Force_matrix[:,j,i]=-F*unit_vector
    
    return np.sum(Force_matrix, axis=1)

def ApplyForces(_objects,h):
    forces = calculateForceVectors(_objects)
    for i in range(len(forces[0,])):
        force = forces[:,i]
        _objects[i].applyForce(force,h)

def update_frame(iteration,_objects):
    pass

def generate_data(_objects,iterations):
    pass    


def draw_animation(Objects,data):
    

    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    # Initialize scatters
    scatters = [(Objects[i].pos[0],Objects[i].pos[1],Objects[i].pos[2]) for i in range(Objects)]

    print(scatters)
    
    # Number of iterations
    iterations = len(data)


    # for i in range(len(Objects)):
    #     print(str(Objects[i]))
    #     axes = plt.subplot(111, projection='3d')
    #     x, y, z = Objects[i].pos
    #     axes.plot(x, y, z, "*", label=f"{Objects[i]}")

    # graph = axes.scatter(Objects.pos[0], 
    #                    Objects.pos[1], 
    #                    Objects.pos[2])

    # fig = plt.figure()

    # ani = animation.FuncAnimation(fig, update_frame, 19, 
    #                               interval=40, blit=False)


    plt.legend(loc="upper right")

    plt.show()


if __name__ == "__main__":
    """
    Ettersom listen "objects" er en liste med objecter som selv
    inneholder deres egen posisjon, trengs det ikke 
    """
    
    h = 10
    objects = getObjectsFromFile()
    sortObjectsToMass(objects)
    ApplyForces(objects,h)
    draw_animation(objects,None)

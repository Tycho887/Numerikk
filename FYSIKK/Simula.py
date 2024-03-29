 # -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:11:55 2022

@author: Michael
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
import copy
import gc
import time

G = 6.6743e-11

class Object:
    
    def __init__(self,mass,position,velocity,name=''):
        self.name = name.strip()
        self.mass = mass
        self.pos = np.array(position)
        self.vel = np.array(velocity)
        self.pos_log = []
        self.energy = 0
        "Position and velocity are 3D vectors"
        
    def applyForce(self,Force,h):
        "h is the interval step length"
        acc_vector = Force/self.mass
        self.vel += acc_vector*h
        #print(Force)
        self.pos += self.vel*h + 0.5*acc_vector*h**2
        self.pos_log.append(copy.deepcopy(self.pos))

    def __str__(self):
        return self.name

    def getPos(self):
        return self.pos_log

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
    return _objects

def gravity_equation(_object1,_object2,_distance):
    "Force from object2 on object1"
    "No need to multiply by mass of object 1"
    "This avoids a division operation per iteration"
    F = (G*_object2.mass*_object1.mass)/_distance**2
    return F

def calculateForceVectors(_objects, force_equation=gravity_equation):
    size = len(_objects)
    Force_matrix = np.zeros(shape=(len(_objects[0].pos),size,size), dtype=float)
    for i in range(len(Force_matrix[0,])):
        for j in range(i+1,len(Force_matrix[0,])):
            
            vector = _objects[i].pos-_objects[j].pos
            distance = np.linalg.norm(vector)
            unit_vector = vector/distance
            F = force_equation(_objects[i],_objects[j],distance)
           # print(F)
            Force_matrix[:,i,j]=F*unit_vector
            Force_matrix[:,j,i]=-F*unit_vector
#             print(f'''vector: {vector}
# distance: {distance}
# unit vector: {unit_vector}
# Force: {F}''')

    "Calculates a matrix of every force between objects"
    "The resultant force on each object is given by the sum of forces along the"
    "1-axis of the 3-d matrix"
    "returns a matrix of forcevectors for each object"
    
    return np.sum(Force_matrix, axis=1)

def ApplyForces(_objects,h):
    forces = calculateForceVectors(_objects)
    for i in range(len(forces[0,])):
        force = forces[:,i]
        _objects[i].applyForce(force,h)
        

def generate_data(_objects,iterations,dt):
    for i in range(iterations):
        print(f'Generating data {i}/{iterations}')
        ApplyForces(_objects, dt)

def curate_data(_objects,iterations):
    for planet in _objects:
        planet.pos_log = planet.pos_log[::100]

def draw_frame(Objects):
    if len(objects[0].pos)==3:
        fig = plt.figure()
        axes = plt.subplot(111, projection='3d')
        for i in Objects:

            freq = len(i.pos_log) # finn en måte å moderere antall punkter som tegnes
            for j in i.pos_log:
                x, y, z = j[0],j[1],j[2]
                axes.plot(x, y, z, "o",color='blue')
            #ax.plot(i.pos[0],i.pos[1],i.pos[2], "o")
    else:
        for i in Objects:
            for j in i.pos_log:
                x,y = j[0],j[1]
                plt.scatter(x,y,s=1,color='blue')
            plt.scatter(i.pos[0],i.pos[1],s=50)
    plt.show()
        
def system_energy(objects):
    pass
    # Finn den totale energien i systemet
        
def find_error(_objects):
    pass
    # Se på total energi før og etter for å finne optimal tidsintervall




if __name__ == "__main__":
    start = time.time()
    gc.collect()
    """
    Ettersom listen "objects" er en liste med objecter som selv
    inneholder deres egen posisjon, trengs det ikke 
    """
    h = 15; iterations = 50000
    objects = getObjectsFromFile('data/earth_moon2d.csv')
    sortObjectsToMass(objects)
    generate_data(objects,iterations,h)
    curate_data(objects, iterations)
    print("Tegner frame")
    
    draw_frame(objects)
    
    print(f'Program runtime: {time.time()-start:.3f} seconds')
    
    #system_energy(objects)
    
    #ApplyForces(objects,h)
    #draw_animation(objects,None)

# def draw_animation(Objects,data):
    

#     # Attaching 3D axis to the figure
#     fig = plt.figure()
#     ax = p3.Axes3D(fig)

#     # Initialize scatters
#     scatters = [(Objects[i].pos[0],Objects[i].pos[1],Objects[i].pos[2]) for i in range(Objects)]

#     print(scatters)
    
#     # Number of iterations
#     iterations = len(data)


#     # for i in range(len(Objects)):
#     #     print(str(Objects[i]))
#     #     axes = plt.subplot(111, projection='3d')
#     #     x, y, z = Objects[i].pos
#     #     axes.plot(x, y, z, "*", label=f"{Objects[i]}")

#     # graph = axes.scatter(Objects.pos[0], 
#     #                    Objects.pos[1], 
#     #                    Objects.pos[2])

#     # fig = plt.figure()

#     # ani = animation.FuncAnimation(fig, update_frame, 19, 
#     #                               interval=40, blit=False)


#     plt.legend(loc="upper right")

#     plt.show()
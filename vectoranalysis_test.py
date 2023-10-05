# -*- coding: utf-8 -*-
"""
Created on Sun May 28 12:13:40 2023

@author: Michael
"""

import numpy as np
import numerikk2 as nm

def F(P):
    x, y, z = P
    return np.array((x,y,z))

def C(t):
    return np.array((1, t, 1/2*t**2))


def derivative(f,x,h=1e-4):
    return (f(x+h)-f(x))/h

S = nm.Vector(F,C).curveIntegral(0, 3)

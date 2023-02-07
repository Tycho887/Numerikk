# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:12:11 2023

@author: Michael
"""
import numpy as np
import sympy as sp
import numerikk2 as nr

def f(x):
    return np.sin(x)

F = nr.Function(f)
F.interval(0,2)
F.draw()

S = F.simpson(); print(S)



# G = nr.Function(g)
#def g(x):
#    return np.exp(x)
#G.draw(0,3)
#x = F.Find_zeros(2); print(x)
#g = F.derivative()
#Bue = F.arclength(); print(Bue)
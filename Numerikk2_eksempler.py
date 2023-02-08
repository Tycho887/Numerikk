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
F.interval(0,np.pi)
F.draw()

S = F.trapes(); print(S)
N = F.buelengde()

# def g(x):
#     return 1/2 * (np.cos(2*x))**2

# G = nr.Function(g,0,2*np.pi)
# S = G.simpson()/3
# print(S)

# G = nr.Function(g)
#def g(x):
#    return np.exp(x)
#G.draw(0,3)
#x = F.Find_zeros(2); print(x)
#g = F.derivative()
#Bue = F.arclength(); print(Bue)
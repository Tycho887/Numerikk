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

F = nr.Function(func=f)
F.interval(0,2*np.pi)
F.draw()

S = F.simpson(); print(S)

#g = F.derivative()
#Bue = F.arclength(); print(Bue)
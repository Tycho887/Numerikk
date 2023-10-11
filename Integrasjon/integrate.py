# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 09:18:34 2023

@author: Michael
"""

import numpy as np
import numerikk2 as nm

def f(x,y):
    return x/x

g1 = lambda x: x**2; g2 = lambda x: 2*x-x**2

def s(xk):
    function = lambda y: f(xk, y)
    F = nm.Function(function)
    F.interval(0, 1,1000)
    return F.integrate()

S = nm.Function(s,0,2)
S.integrate()


# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:12:11 2023

@author: Michael
"""
import numpy as np
from numerikk2 import *

def f(x):
    return np.sin(x)

F = Function(func=f)
F.interval(0,3.14)
F.draw()

S = F.simpson(); print(S)

Bue = F.arclength(); print(Bue)
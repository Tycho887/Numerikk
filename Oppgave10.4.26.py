# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:45:58 2023

@author: Michael
"""

import numerikk2 as nm
import numpy as np

def r1(t):
    return 1-np.cos(t)

def r2(t):
    return -1+np.sin(t)

R1 = nm.Function(r1)
R2 = nm.Function(r2)

R1.draw(polar=True)
R2.draw(0,10)
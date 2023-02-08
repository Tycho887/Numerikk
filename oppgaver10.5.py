# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 13:04:29 2023

@author: Michael
"""

import numerikk2 as nm
import numpy as np

"Oppgave 10.5.6"

def r(t):
    return abs(np.cos(3*t))

F = nm.Function(r,-np.pi/6,np.pi/6)
F.draw(polar=True)
A = F.polar_area()
print(A)

"Oppgave 10.5.21"

h = lambda t : t**2
H = nm.Function(h,0,np.sqrt(5),polar=True)
H.draw()
L=H.buelengde()
print(L)

"Oppgave 10.5.21"

h = lambda t : np.exp(t)/np.sqrt(2)
H = nm.Function(h,0,np.pi,polar=True)
H.draw()
L=H.buelengde()
print(L)
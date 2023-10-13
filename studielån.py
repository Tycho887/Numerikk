# -*- coding: utf-8 -*-
"""
Created on Sat May 20 18:42:22 2023

@author: Michael Johansen
"""
import matplotlib.pyplot as plt
import numpy as np
from math import *

rente = 1.01
årlig = 82744

def lån(år):
    return årlig*np.ceil(år)*rente**år

periode = np.linspace(0,7,100)

plt.scatter(periode,lån(periode))
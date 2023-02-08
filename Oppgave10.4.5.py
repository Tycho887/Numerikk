# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:35:11 2023

@author: Michael
"""

import numerikk2 as nm
import numpy as np


def r(t):
    return 1+np.cos(t)

R = nm.Function(r)

R.draw(n=50,polar=True)
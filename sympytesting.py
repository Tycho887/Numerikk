# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:05:34 2023

@author: Michael
"""

import sympy as sp
import numpy as np

def f(x):
    return np.sin(x)

k = sp.Symbol('k')

x = sp.sympify(f)

deriv_x = sp.lambdify(k, sp.diff(x(k)))

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:05:34 2023

@author: Michael
"""

import sympy as sp
import numpy as np

k = sp.Symbol('k')

# def f(x):
#     return np.sin(x)

# x = sp.sympify(f)

# deriv_x = sp.lambdify(k, sp.diff(x(k)))

def f(x):
    return np.sin(x)

def x(p):
    return sp.sympify(f(k))(p)

def deriv_f(t):
    return sp.lambdify(k,sp.diff(f(k)))(t)
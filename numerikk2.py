# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:39:05 2022

@author: Michael
"""

import numpy as np
import matplotlib.pyplot as plt
from math import factorial as fact
import math
import scipy


# class Calculus:
#     def __init__(self,func):
#         self.func = func
#         pass
#     def derivative(self):
#         assert callable(func)
#         assert isinstance(x, (int, float))
#         assert isinstance(h, float)
#         if   order==1:
#             return (func(x+h)-func(x))/h
#         elif order==2:
#             return (func(x+h)-2*func(x)+func(x-h))/(h**2)
#         elif order > 2:
#             h = 1e-2 # roundoff error blir for stor hvis h er mindre
#             Sum = 0
#             n = order
#             for k in range(0,order+1):
#                 # benytter binomial koeffisienter
#                 Sum += ((-1)**(k+n) * scipy.special.comb(order,k) * func(x + k*h))
#             Sum *= 1/h**n
#             #print(scipy.special.comb(order,k))
#     def newton(self):
#         pass
#     #def 



class Function:
    def __init__(self,a,b,func,n=100):
        """
        a: float or list/array. Either start value or list/array
           containing data.
        b: end point of interval.
        n: number of intervals
        """
        self.a = a; self.b = b; self.n = n
        self.func = func
        self.x = np.linspace(self.a,self.b,self.n+1)
        self.y = self.func(self.x)
        self.dx = (self.b-self.a)/self.n
        self.S = 0
        self._setup_internal()
        
    def _setup_internal(self):    
        self.S = self.y[0]+self.y[-1]
        return self.S
        
    def trapes(self):
        self._setup_internal()
        self.S += sum([2*i for i in self.y[1:-1]])
        self.S *= 0.5*self.dx
        return self.S
    
    def simpson(self):
        self._setup_internal()
        self.S += sum([4*i for i in self.y[1:-1:2]])+sum([2*i for i in self.y[2:-1:2]]) 
        self.S *= (self.dx/3)
        return self.S    
    
    def midtpunkt(self):
        self._setup_internal()
        self.S += sum([self.func(i) for i in list(self.x[:-1]+(self.dx/2))])
        self.S *= self.dx
        return self.S
    
    def interval(self,a,b,n=None):
        self.a = a
        self.b = b
        self._setup_internal()
        if n!=None:
            self.n = n
        return self.a,self.b,self.n
    
    # def derivative(self,x,order=1,h=0.001):
    #     if order==1:
    #         return (func(x+h)-func(x))/h
    #     elif order==2:
    #         return (func(x+h)-2*func(x)+func(x-h))/(h**2)
    def draw(self):
        plt.plot(self.x,self.y)
        plt.show()
        
    
    
a = 0; b = 7 # f = lambda x : x**2

def f(x):
    return np.sin(x)

j = lambda i : i**2

F = Function(a,b,func=f)
J = Function(a,b,func=j)

F.draw()
        
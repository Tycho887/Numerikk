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
import sympy as sp


#Sympy symboler
t = sp.Symbol('t')

class Function:
    def __init__(self,func,a=None,b=None,n=1e4):
        """
        a: float or list/array. Either start value or list/array
           containing data.
        b: end point of interval.
        n: number of intervals
        """
        self.func = func
        
        #Definer skjente nullpunkter
        self.deriv_func = None
        self.zeros = []
        
        #Definer området før du kan arbeide
        self.a = a; self.b = b;
        
        #Definer x og y punkter
        self.n = math.ceil(n) # antall inndelinger
        self.dx = None
        self.x = None
        self.y = None
        
        #Definer integralsummen
        self.S = None
        
        #misc
        self.h = 1e-5
        

    
    "Oppsett"
    
    def interval(self,a,b,n=None):
        if a!=None and b!=None:
            self.a = a
            self.b = b
            if n!=None:
                self.n = n
        return self.a,self.b,self.n
    
    def _setup_values(self):
        if self.a==None or self.b==None:
            raise ValueError("Parametere er udefinert")
        self.x = np.linspace(self.a,self.b,self.n+1)
        self.dx = (self.b-self.a)/self.n
        self.y = self.func(self.x)
        return self.x,self.y,self.dx
    
    "Derivering"
    
    def derivative(self,x):
        return (self.func(x+self.h)-self.func(x))/self.h
    def second_deriv(self,x):
        return (self.func(x+self.h)-2*self.func(x)+self.func(x-self.h))/(self.h**2)
        
        # self.deriv_func = sp.lambdify(t, sp.diff(self.func(t)))
        # return self.deriv_func
    
    "Newtons metode"
    
    def Find_zeros(self,func,x):
        pass
    
    "Integrering"
    
    def _setup_integral(self):
        self._setup_values()
        self.S = self.y[0]+self.y[-1]
        return self.S
        
    def trapes(self):
        self._setup_integral()        
        self.S += sum([2*i for i in self.y[1:-1]])
        self.S *= 0.5*self.dx
        return self.S
    
    def simpson(self):
        self._setup_integral()
        self.S += sum([4*i for i in self.y[1:-1:2]])+sum([2*i for i in self.y[2:-1:2]]) 
        self.S *= (self.dx/3)
        return self.S    
    
    def midtpunkt(self):
        self._setup_integral()
        self.S += sum([self.func(i) for i in list(self.x[:-1]+(self.dx/2))])
        self.S *= self.dx
        return self.S
    
    "Buelengde"

    def arclength(self):
        self._getDerivativeFunc()
        main_func = self.func
        S = self._tempfunc(1)
        
    "Visualisering"
    
    def draw(self,a=None,b=None,n=None):
        self.interval(a, b, n)
        self._setup_values()
        plt.plot(self.x,self.y)
        plt.show()

class Sympy:
    def __init__(self):
        pass
    def derivative(self):
        pass
    def arclength():
        pass
    def newton():
        pass
    
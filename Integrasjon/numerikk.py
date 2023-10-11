# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:14:58 2022

@author: Michael
"""

import numpy as np
from math import factorial as fact
import matplotlib.pyplot as plt
import time
import math
import scipy

# comment

def internal_deriv(func, x, dx=1e-5, order=1):
    assert callable(func)
    assert isinstance(x, (int, float))
    assert isinstance(dx, float)
    if   order==1:
        return (func(x+dx)-func(x))/dx
    elif order==2:
        return (func(x+dx)-2*func(x)+func(x-dx))/(dx)**2
    elif order > 2:
        raise Exception('order må være 1 eller 2')


class calc:
    """
    Numeriske metoder fra kalkulus faget
    """
    def rectangle(func=None, array=None, start=-100, stopp=100, n=100, data=False):
        """
            DESCRIPTION. 
            regner ut arealet under grafen ved bruk av enkel rektangel metode.
            gi en function hvis data==False, ellers gi en liste/array
            for å regne med importert data.
        """
        if data==True:
            try:
                Sum = 0
                for i in array[:-1]:
                    Sum += i
                return Sum

            except ValueError:
                print('Argument må være liste/array')
        else:
            try:
                dx = (stopp-start)/n
                x = np.linspace(start, stopp, n+1)
                Sum = 0
                for i in x[:-1]:
                    Sum += func(i)*dx
                return Sum
            except ValueError:
                print('Argument må være function, start, stopp, antall')
        
    def midtpunkt(func=None, array=None, start=-100, stopp=100, n=100, data=False):
         """
            DESCRIPTION. 
            regner ut arealet under grafen ved bruk av midtpunkts metode.
            gi en function hvis data==False, ellers gi en liste/array
            for å regne med importert data.
         """
         
         assert isinstance(data, bool)
         
         if data==True:
             
             try:
                 x = array
                 Sum = 0
                 for idx, item in enumerate(x[:-1]):
                     Sum += item + x[idx+1]
                 return (1/2)*Sum
             
             except ValueError:
                     print('Argument må være liste/array')

         else:
             try:
                dx = (stopp-start)/n
                x = np.linspace(start, stopp, n+1)
                Sum = 0
                for idx, item in enumerate(x[:-1]):
                     Sum += func((item + x[idx+1])/2)*dx
                return Sum
             except ValueError:
                 print('Argument må være function, start, stopp, antall')

    
    def trapes(func=None, array=None, deriv2=None, expected_value=None, start=-100, stopp=100, n=100, data=False):
        """
            DESCRIPTION. 
            regner ut arealet under grafen ved bruk av trapes metode.
            gi en function hvis data==False, ellers gi en liste/array
            for å regne med importert data.
            deriv2 er andrederivert av funksjonen f.
        """
        if data==True:
            try:
                Sum = array[0]+array[-1]
                for i in array[1:-1]:
                    Sum += 2*i
                return Sum*(0.5)
            
            except ValueError:
                print('Argument må være liste/array')

        else:
            try:
                dx = (stopp-start)/n
                x = func(np.linspace(start,stopp,n+1))
                Sum = x[0]+x[-1]
                for i in x[1:-1]:
                    Sum += 2*i
                Sum *=(dx/2)
                    
                if isinstance(expected_value, (int,float)):
                    if not callable(deriv2) and not isinstance(deriv2, (int,float)):
                        raise Exception('deriv2 må være en funksjon eller float')
                    elif callable(deriv2):
                        M  = np.max(deriv2(x))
                    elif isinstance(deriv2, (int,float)):
                        M = deriv2
                        
                    ET = M*(stopp-start)**3/(12*n**2)
                    abs_ET = Sum/expected_value
    
                    return Sum, ET, abs_ET
                else:
                    return Sum
    
            except ValueError:
                print('Argument må være function, start, stopp, antall')

        
    
    
    def simpson(func=None, array=None, deriv4=None, expected_value=None, start=-100, stopp=100, n=100, data=False):
        """
            DESCRIPTION. 
            regner ut arealet under grafen ved bruk av simpsons metode.
            gi en function hvis data==False, ellers gi en liste/array
            for å regne med importert data.
            deriv4 er fjerdederivert av funksjonen f.
        """
        Sum = 0
        
        if data==True:
            try:
                Sum = array[0]+array[-1]
                for i in array[1:-1:2]:
                    Sum += 4*i
                for j in array[2:-1:2]:
                    Sum += 2*j
                return (1/3)*Sum
               
            except ValueError:
                print('Argument må være liste/array')

        else:
            if array is None:
                raise SyntaxError('Angi data = True')
            try:
                dx = (stopp-start)/n
                x = np.linspace(start,stopp,n+1)
                Sum = func(x[0])+func(x[-1])
                for i in x[1:-1:2]:
                    Sum += 4*func(i)
                for j in x[2:-1:2]:
                    Sum += 2*func(j)
                Sum *=(dx/3)
                
                if isinstance(expected_value, (int,float)):
                    if not callable(deriv4) and not isinstance(deriv4, (int,float)):
                        raise Exception('deriv4 må være en funksjon eller float')
                    elif callable(deriv4):
                        M  = np.max(deriv4(x))
                    elif isinstance(deriv4, (int,float)):
                        M = deriv4
                        
                    ES = M*(stopp-start)**5/(180*n**4)
                    abs_ES = Sum/expected_value
    
                    return Sum, ES, abs_ES
                else:
                    return Sum
            
            except ValueError:
                print('Argument må være function, start, stopp, antall')
    
    def riemann(y_array=None, x_array=None):
        """
        Riemann summering er en god måte for å
        estimere integralet under en graf når intervallene
        er variable
        """
        dx=[]; Sum=0
        for x1, x2 in zip(x_array, x_array[1:]):
            dx.append(x2-x1)
        for idx, y in enumerate(y_array[:1]):
            Sum = y*dx[idx]
            
        return Sum
    
    def derivative(func=None, x=None, x_array=None, y_array=None, h=None, order=1, data=False):
        """
        Description
        Numerisk utregning av den deriverte
        til en funksjon f i et punkt x, oppgi orden
        enten 1, 2 eller n (lang computation time)
        """
        if data==False:
            if h==None:
                h=1e-5
            assert callable(func)
            assert isinstance(x, (int, float))
            assert isinstance(h, float)
            if   order==1:
                return (func(x+h)-func(x))/h
            elif order==2:
                return (func(x+h)-2*func(x)+func(x-h))/(h**2)
            elif order > 2:
                h = 1e-2 # roundoff error blir for stor hvis h er mindre
                Sum = 0
                n = order
                for k in range(0,order+1):
                    # benytter binomial koeffisienter
                    Sum += ((-1)**(k+n) * scipy.special.comb(order,k) * func(x + k*h))
                Sum *= 1/h**n
                #print(scipy.special.comb(order,k))
                
                
                return Sum
        else:
            if (not x_array is None) and y_array is None: 
                raise ValueError('Du må spesifisere x og y lister')            
            if h==None:
                h=1
            else:
                h = []
                for x0, x1 in zip(x_array,x_array[1:]):
                    h.append(x1-x0)
                    
            if order==1: 
                y = []
                if x_array is None:
                    for i, val in enumerate(y_array[:-1]):
                        deriv = (y_array[i+1]-y_array[i])/h
                        y.append(deriv)
                elif isinstance(x_array, (tuple,list,np.ndarray)):
                    for i in range(len(y_array)-1):
                        deriv = (y_array[i+1]-y_array[i])/h[i]
                        y.append(deriv)
                else:
                    raise ValueError('Type må være array eller array-like')
                y.append(y[-1])
                y = np.array(y)
                return y
            
            elif order==2:
                y = []
                if x_array is None:
                    for i, val in enumerate(y_array[1:-1]):
                        deriv = (y_array[i+1]-2*val+y_array[i-1])/h**2
                        y.append(deriv)
                elif isinstance(x_array, (tuple,list,np.ndarray)):
                        deriv = (y_array[i+1]-2*val+y_array[i-1])/h[i]**2
                        y.append(deriv)
                y.append(y[-1]); y.insert(0, y[0])
                y = np.array(y)
                return y
            elif order > 2:
                raise Exception('Kan ikke nte-derive data fra fil enda')
                # Sum = 0
                # n = order
                # for k in range(0,order):
                #     # benytter binomial koeffisienter
                #     Sum += (-1)**k*n * (fact(n)/(fact(k)*fact(n-k))) * func(x + k*h)
                # Sum *=h**n
                # return Sum
            else:
                raise Exception('ulovlig order verdi')
            
            
    def newton(func, start, tol=1e-5, iterations=100, f_deriv=None):
        """
        Finner nullpunkter til en funksjon ved
        bruk av Newtons metode. Hvis mulig kan du
        oppgi en funksjon for den deriverte f_deriv.
        Hvis ikke du vet hva den er kan du la feltet
        være blank, og den deriverte vil bli utregnet
        numerisk.
        """
        assert callable(func)
        assert isinstance(start, (int, float))
        if callable(f_deriv):
            xn = start; i = 0
            while not abs(func(xn))<tol and i < iterations:
                i  += 1
                xn -= (func(xn)/f_deriv(xn))
            return xn, func(xn)
        elif not callable(f_deriv) and f_deriv==None:
            xn = start; i = 0
            while not abs(func(xn))<tol and i < iterations:
                 i  += 1
                 xn -= func(xn)/internal_deriv(func, xn)
            return xn, i
            
                        
class linalg:
    """
    numeriske metoder fra lineær algebra
    """
    def euler(func, stopp, t0, y0, h=1e-3, numsteps=None):
        """
        Numerisk løsning av førsteordens ODE
        ved bruk av Eulers metode. Gir tilbake
        numpy lister for enkel visualisering
        """

        if stopp < t0:
            raise Exception('Sluttverdi må være større enn startverdi')
        else:
            yn = y0 + func(t0, y0)*h
            t  = np.arange(t0,stopp,h)
            y  = [yn]
            i = 1
            for n in t[:-1]:
                if numsteps!=None:
                    if i > numsteps:
                        break
                i += 1
                yn = yn + func(t0+h**i, yn)*h
                y.append(yn) 
            y = tuple(y)
            return t, y
    
    def heun(func, stopp, t0, y0, h=1e-3):
        """
        Numerisk løsning av førsteordens ODE
        ved bruk av Heuns metode. Gir tilbake
        numpy lister for enkel visualisering
        """
        if stopp < t0:
            raise Exception('Sluttverdi må være større enn startverdi')
        else:
            yn = y0 + func(t0, y0)*h
            t  = np.arange(t0,stopp,h)
            y  = []
            i = 1
            for n in t:
                i += 1
                Yi = yn + func(t0+h*i, yn)*h
                yn = yn + (h/2)*(func(t0+h**i,yn)+func(t0+h*(i+1),Yi))
                y.append(yn)
            y = tuple(y)
            return t, y
        
class inf:
    """
    ofte brukte funksjoner i INF120
    """
    def C2F(C):
        "omgjør fra celsius til fahrenheit"
        return (9/5)*C + 32

    def F2C(F):
        "omgjør fra fahrenheit til celsius"
        return (F-32) * 5/9

    def C2K(C):
        "omgjør fra celsius til Kelvin"
        return C-273.15

    def K2C(K):
        "omgjør fra Kelvin til celsius"
        return K+273.15

    def F2K(F):
        "omgjør fra fahrenheit til Kelvin"
        return ((F-32) * 5/9)-273.15

    def K2F(K):
        "omgjør fra Kelvin til fahrenheit"
        return (9/5)*(K-273.15) + 32
    
class misc:
    """
    miscellaneous/diverse personlige prosjekter
    """
    def mandelbrot(height=512, zoom=1, frame = 3.6, focus=(-0.5,0), runtime=False, auto_out=True, cmap='magma'):
        """
        Generer et mandelbrot plot med focus i (focus)
        og størrelse basert på pixelhøyde og frame
        
        """
        start_time = time.time()
        
        def bound_check(c, depth=100):
            z = 0; iterations = 0
            flag = False
            while iterations < depth:
                if not abs(z) < 2:
                    break
                z = z**2 + c; iterations += 1
            else:       # kjører dersom det er en break i while loopen
                flag = True
            return flag, iterations
        
        x_start = focus[0]-frame/(2*zoom)
        x_stop  = focus[0]+frame/(2*zoom)
        y_start = focus[1]-frame/(2*zoom)
        y_stop  = focus[1]+frame/(2*zoom)
        image_format = round(abs(x_stop-x_start)/abs(y_stop-y_start))
        width = math.floor(height*image_format)
        x_range = np.arange(x_start, x_stop, (x_stop-x_start)/width)
        y_range = np.arange(y_start, y_stop, (y_stop-y_start)/height)
        image = np.zeros((width,height), dtype=float); leng = len(x_range)
        
        for i, x in enumerate(x_range):
            print(f'{i:<4} ut av {(leng):>4}; {100*i/leng:.2f}%')
            for j, y in enumerate(y_range): 
                flag, iters = bound_check(complex(x,y))
                if flag == True:
                    image[i, j] = 0
                else:
                      image[i, j] = math.log(iters)
        
        if auto_out==True:
            plt.imshow(image.transpose(), interpolation='nearest', cmap=cmap)        
            plt.title(f'Mandelbrot set; {height}x{height*image_format:.0f} pixels')
            plt.show()
            print(f'------- runtime was {(time.time() - start_time):.1f} seconds -------')
            
        if runtime==False:
            return image 
        else:
            return image, time.time-start_time
        
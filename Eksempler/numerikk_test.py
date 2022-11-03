from numerikk import calc, linalg, misc
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = 'øvingsoppgaver/modul 5/dat/acc.dat'

df = np.array(pd.read_csv(file, sep=(';')))
df.reshape(len(df),1)

#x1 = np.arange(0,100)

#print('simson', calc.simpson(func=f, n=4, start=0, stopp=2, deriv4=0, expected_value=6))

#print('trapes', calc.trapes(func=f, n=4, start=0, stopp=2, deriv2=f_d, expected_value=6))

#oppgave 2.10.12


# def f(t):
#     return t**3 + t

# def f_d(x):
#     return 6*x

# def g(x):
#     return np.exp(x)

def F1(t, y):
    return np.sin(2*np.pi*t) + t*y 

t1, y1 = linalg.euler(func=F1, stopp=1, t0=0, y0=1, h=0.01)

def F2(t, y):
    return y**3


t1, y1 = linalg.euler(func=F2, stopp=2, t0=1, y0=0.5, h=0.1)
t2, y2 = linalg.heun(func=F2, stopp=2, t0=1, y0=0.5, h=0.1)
plt.plot(t1,y1)
plt.plot(t2,y2); plt.show()
from numerikk import calc, linalg, misc
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# dersom du ønsker å integrere akselerasjonsdata i en fil

file = 'data/acc.dat'
dataframe = np.array(pd.read_csv(file, sep=(';')))
dataframe.reshape(len(dataframe),1)

print(calc.simpson(array=dataframe, data=True))



#%%

def f(t):
    return t**3 + t

def f_d(x):
    return 6*x

def g(x):
    return np.exp(x)

print('simson', calc.simpson(func=f, n=4, start=0, stopp=2, deriv4=0, expected_value=6))

print('trapes', calc.trapes(func=f, n=4, start=0, stopp=2, deriv2=f_d, expected_value=6))

#%%

def F1(t, y):
    return np.sin(2*np.pi*t) + t*y 

def F2(t, y):
    return y**3

t1, y1 = linalg.euler(func=F1, stopp=1, t0=0, y0=1, h=0.01)
t2, y2 = linalg.euler(func=F2, stopp=2, t0=1, y0=0.5, h=0.1)
t3, y3 = linalg.heun(func=F2, stopp=2, t0=1, y0=0.5, h=0.1)
plt.plot(t1,y1); plt.plot(t3,y3)
plt.plot(t2,y2); plt.show()
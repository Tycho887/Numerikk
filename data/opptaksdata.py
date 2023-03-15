# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 21:46:13 2023

@author: Michael
"""

import numpy as np
import matplotlib.pyplot as plt

def get_data():
    with open('karakterdata.csv', 'r') as datalist:
        yr = []; gr = []
        for data in datalist:
            a, b = data.split()
            yr.append(int(a))
            gr.append(float(b))
        
    return np.array(yr), np.array(gr)
years, grades = get_data()
print(f'''
Median: {np.mean(grades):.2f}
Avvik:  {max(abs(grades-np.mean(grades))):.2f}
Høyeste noensinne: {max(grades):.2f}
''')
plt.plot(years,grades)
plt.show()
"""
Sample script to plot a bifurcation diagram 
"""

import matplotlib.pyplot as plt
import numpy as np 
from itertools import groupby

#Read in data
data = np.genfromtxt( .... )
x, y, stability = np.hsplit(data, 3)

#Group according to stability
for g_z, group in groupby(zip(zip(x, y), stability), lambda p: p[1]):
    g_x, g_y = [], []
    for i in group:
        g_x.append(i[0][0])
        g_y.append(i[0][1])
        
    #Plot as dashed or solid line according to stability
    if g_z:
        plt.plot(g_x, g_y, linestyle='--', color='m', linewidth=2.0)
    else:
        plt.plot(g_x, g_y, linestyle='-', color='m', linewidth=3.5)
        
plt.show()
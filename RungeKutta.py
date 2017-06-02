# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:43:34 2017

@author: njgh002
"""


import numpy as np
np.set_printoptions(threshold=np.inf)           #shows entire array. does not have ... in it
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def tank(h,t):
    c1 = 0.13
    c2 = 0.20
    Ac = 2.0
    
    if t > 0.5:
        qin = 1.5
    else:
        qin = 0.5
        
    qout1 = c1 * h[0]**0.5
    qout2 = c2 * h[1]**0.5
    dhdt1 = (qin - qout1)/Ac
    dhdt2 = (qout1 - qout2)/Ac
    
    dhdt = [dhdt1 , dhdt2]
    return dhdt

tank([0.25,0.5],0.5)

h0 = [0,0]
t = np.linspace(0,10,21)
y = odeint(tank,h0,t)

plt.plot(t,y[:,0], 'b-')
plt.plot(t,y[:,1], 'r--')
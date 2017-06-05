# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:37:25 2017

@author: njgh002
"""
import numpy as np
#np.set_printoptions(threshold=np.inf)           #shows entire array. does not have ... in it
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def tank(h,t,c1,c2):
    Ac = 2.0
    if t>0.5:
        qin = 0.5
    else:
        qin = 0.5
        
    qout1 = c1 * h[0]**0.5
    qout2 = c2 * h[1]**0.5
    
    dhdt1 = (qin-qout1)/Ac
    dhdt2 = (qout1-qout2)/Ac 
    if h[0] >= 1 and dhdt1>0:
        dhdt1 = 0
        
    if h[1] >= 1 and dhdt2>0:
        dhdt2 = 0
        
    dhdt  = [dhdt1, dhdt2]
    return dhdt

h0 = [0,0]
t= np.linspace(0,10,21)
c= (0.13,0.20)
y = odeint(tank,h0,t,c)       #outputs an array

plt.plot(t,y[:,0], 'b-')
plt.plot(t,y[:,1], 'r--')
plt.xlabel('Time (hrs)')
plt.ylabel('Height (m)')
plt.legend(['h1','h2'])
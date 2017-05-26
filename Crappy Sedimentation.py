# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:37:40 2017

@author: njgh002
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf) #shows entire array. does not have ... in it


def f(m):
    sigma   = 1000      #M/min
    endtime = 2
    timestep= 100
    array   = np.zeros(timestep)
    
    for i in np.arange(0 , endtime, timestep):
        
        dmdt     = sigma - r(m)
        array[i] = dmdt
        return array
        
    

def r(m):
    g = 0.278   #1/min
#    m    = 100      #number of monomers (M)
    
    dmdd  = g * m
    
    return dmdd


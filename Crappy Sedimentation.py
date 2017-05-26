# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:37:40 2017

@author: njgh002
"""

import numpy as np
<<<<<<< HEAD
np.set_printoptions(threshold=np.inf)           #shows entire array. does not have ... in it
#from scipy.integrate import odeint
#import matplotlib.pyplot as plt
=======
from scipy.integrate import odeint
import matplotlib.pyplot as plt
>>>>>>> 534d8f5ca5d690dd16516520131b4d2d06e32945



def f(m):
    sigma   = 1000      #M/min
<<<<<<< HEAD
    endtime = 15
    timestep= 1
    array   = np.zeros(endtime)
    
    for i in range(0,endtime,timestep):
        dmdt     = sigma - r(m)
        array[i] = dmdt
    return array
=======
    endtime =
    timestep=
    array   = np.zeros(timestep)
    
    for i in np.arange(0 , endtime, timestep)
        
        dmdt     = sigma - r(m)
        array[i] = dmdt
        return array
>>>>>>> 534d8f5ca5d690dd16516520131b4d2d06e32945
        
    

def r(m):
    g = 0.278   #1/min
#    m    = 100      #number of monomers (M)
    
    dmdd  = g * m
    
    return dmdd

<<<<<<< HEAD
f(10)

=======
>>>>>>> 534d8f5ca5d690dd16516520131b4d2d06e32945

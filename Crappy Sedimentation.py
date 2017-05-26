# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:37:40 2017

@author: njgh002
"""

import numpy as np
np.set_printoptions(threshold=np.inf)           #shows entire array. does not have ... in it
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def f():
    
    sigma   = 1      #M/min
    m       = 10**-6     # num of monomers
    endtime = 10
    timestep= .9
    timearray   = np.arange(0,endtime,timestep)
    
    #find size of array
    for i in range(0,len(timearray)):
        dmdt     = sigma - r(m)
        timearray[i] = dmdt
        m        = m + dmdt
    return timearray

       
    

def r(m):
    g    = 0.278   #1/min
    c    = 500
    fmd  =  m * g
#    fmd  = 2*c*m**2
    return fmd

f()

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:33:31 2017

@author: njgh002
"""
import numpy as np
np.set_printoptions(threshold=np.inf)           #shows entire array. does not have ... in it
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def smodel():
    """Runs entire model"""
    
    m = 10**-6


def arraymaker(numarray,endtime,timestep):
    """creates n number of arrays based on 
    the endtime and timestep that is specified"""    
    
    manyarrays = [0]*numarray
    for i in range(0,numarray):
        array = np.arange(0,endtime,timestep)
        manyarrays[i] = array
    return manyarrays

arraymaker(3,4,2)
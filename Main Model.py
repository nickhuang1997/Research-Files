# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:47:24 2017

@author: njgh002
"""
import numpy as np
np.set_printoptions(threshold=np.inf)           #shows entire array. does not have ... in it
import matplotlib.pyplot as plt
#==============================================================================
#Sedimentation Model 
# Assumptions
#   1. system is well stirred
#   2. bubbles float straight verticle
#==============================================================================



vel_k       = .01

def sedimentation():
    arrayradius = np.zeros(5)                   #creates an array with the same amount of slots as sailors
    radius_k    = .001
    timestep    = .0001
    endtime     = 2
    
    for i in np.arange(0,endtime,timestep):
        radius_k += .04
        arrayradius[i] = radius_k
    
    plt.xlabel('Radius of Particle')
    plt.ylabel('Number of Occurances')
    plt.hist(arrayradius,bins =5,histtype="bar")          #could use bins = 'auto'

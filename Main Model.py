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

sedimentation()
#    arraypos = np.zeros(sailors)                   #creates an array with the same amount of slots as sailors
#    for i in range(0, sailors):
#        endpos = walkfunc(nsteps)
#        arraypos[i] = endpos
#        
#        vel_k    += 
        
        

##Radius         model
#def rk():             #for rising particle of radius k 
#
#
#
##Velocity       model 
#def vel_k():
#
#
#
##Area           model
#def ak(rk):                 #area of rising particle. which is spherical
#
#
#
##concentration  model
#c1  =        #concentration of solution
#
#

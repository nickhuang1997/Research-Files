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
    
    sigma   = 1      #M/min
    m       =10**-6    # num of monomers
    endtime = 5
    timestep= .1
    
    numarray = int(input('How many arrays of data are you comparing? '))
    xarrays = arraymaker(numarray,endtime,timestep)
    
    for i in range(0,len(xarrays[0])):
        xarrays[i][i]  = linearODE(sigma,m)
        m              = m + dmdt1
        
    x = range(0,len(xarrays[0]))
    y = xarrays[0]
    
    y2= xarrays[1]
    print(y)
    print(y2)
    
    
    plt.plot(x,y, label = 'Gamma Line')
    plt.plot(x,y2, label = "m^2 Line")
    plt.xlabel('Time (min)')
    plt.ylabel('Concentration... in mM')
    plt.legend()
    plt.title('Rate of change of concentration of monomer LTB4 over time')    
#        for z in range(0,numarray):
            
#            xarrays[i][z]  = nonlinearODE(sigma,m) 
               
#    plt.plot(x,y, label = 'Gamma Line')
#    plt.plot(x,y2, label = "m^2 Line")
#    plt.xlabel('Time (min)')
#    plt.ylabel('Concentration... in mM')
#    plt.legend()
#    plt.title('Rate of change of concentration of monomer LTB4 over time')
        
        
    
def arraymaker(numarray,endtime,timestep): 
    """creates n number of arrays based on 
    the endtime and timestep that is specified"""    
    
    manyarrays = [0]*numarray
    for i in range(0,numarray):
        array = np.arange(0,endtime,timestep)
        manyarrays[i] = array
    return manyarrays



def linearODE(sigma, m):
    """calculates the m * g"""
    g     = 0.278
    fmd1  = g * m
    dmdt1 = sigma - fmd1
    return dmdt1


    
def nonlinearODE(sigma, m):
    """calculates value for nonlinear ode"""
    c1   = 1
    fmd2 = 2 * c1 * m**2
    dmdt2= sigma - fmd2
    return dmdt2

    

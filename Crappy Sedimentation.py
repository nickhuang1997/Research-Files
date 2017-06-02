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
        m       =10**-6    # num of monomers
        q       = 10**-6
        endtime = 5
        timestep= .0001
        timearray   = np.arange(0,endtime,timestep)
        timearray2  = np.arange(0,endtime,timestep)
        
    
        for i in range(0,len(timearray)):
            dmdt            = sigma - r(m) 
            timearray[i]    = dmdt
            m               = m + dmdt
            
    
            dmdt2           = sigma - s(q)
            timearray2[i]   = dmdt2
            q               = q + dmdt2
            
            
        x = range(0,len(timearray))
        y = timearray
        
        y2= timearray2
        print(y)
        print(y2)
        
        
        plt.plot(x,y, label = 'Gamma Line')
        plt.plot(x,y2, label = "m^2 Line")
        plt.xlabel('Time (min)')
        plt.ylabel('Concentration... in mM')
        plt.legend()
        plt.title('Rate of change of concentration of monomer LTB4 over time')
        

    

def r(m):

    g    = 0.278   #1/min
    fmd  =  m * g

#    c    = 1.3
#    fmd  = 2*c*m**2
    return fmd

def s(q):
    
    c1  = 1       #constant value
    
    fmd2 = c1*q**2
    
    return fmd2
#def d(m):
#    c1   = 
#    dddt = c1 * m**2
#    return dddt 




f()

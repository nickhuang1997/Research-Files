# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 18:30:19 2017

@author: Nick
"""

import numpy as np
np.set_printoptions(threshold=np.inf)           #shows entire array. does not have ... in it
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def main(y0,t):
    """
    runs differential portion
       
    the formula used is:
           -A*x**b 
    """
    
    A    = 10       #initial A value
    x    = 5 #10**-6  #starting concentration of LTB4
    dmdt = [0]*3    #creates array [0,0,0]
    b    = .5       #initial b value
    j    = .5       #value that b changes by
    
    for i in range(0,3):
        
        dmdt[i] = -A*x**b
        
        b   += -j   #subtracts value from b 
    
    return dmdt

def graph():
    """
    solves dmdt
    graphs the values from main()
    """
        
    y0 = [0,0,0]
    t  = np.linspace(0,10,50)  #(t start,t stop,number)
    y  = odeint(main,y0,t)      #Solves dmdt and puts in array

    plt.plot(t,y[:,0], 'b-')
    plt.plot(t,y[:,1], 'r--')
    plt.plot(t,y[:,2], 'p')
    
    plt.xlabel('Time (mins)')
    plt.ylabel('LTB4 Concentration')
    plt.legend(['b1','b2','b3'])


graph()
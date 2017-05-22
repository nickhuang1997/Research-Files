# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:17:07 2017

@author: Nick
"""

#Walk Funct
import random
import numpy as np
np.set_printoptions(threshold=np.inf)           #shows entire array. does not have ... in it
import matplotlib.pyplot as plt



def walkfunc(nsteps):
    
    pos = 0                                     # initial position of sailor    
    
    for z in range(0, nsteps):
        FwdOrBack = random.choice([1,2])        #1 = fwd 2 = back
        
        if FwdOrBack == 1:
            pos = pos + 1
       
        else:
            pos = pos - 1
        
    return pos


def manysailors():
    sailors = int(input('How many sailors are there? '))
    nsteps = int(input('How many steps will each sailor take? '))
    arraypos = np.zeros(sailors)                   #creates an array with the same amount of slots as sailors
    for i in range(0, sailors):
        endpos = walkfunc(nsteps)
        arraypos[i] = endpos
    
#    bins = np.arange(-nsteps,nsteps)
    plt.xlabel('Final Position')
    plt.ylabel('Number of sailors')
    plt.hist(arraypos,bins ='auto',histtype="bar")          #could use bins = 'auto'
#    plt.savefig('users/nick/desktop/Many_sailors.png')

manysailors()
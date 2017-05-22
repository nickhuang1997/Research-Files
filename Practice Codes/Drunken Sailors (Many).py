# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:17:07 2017

@author: Nick
"""

#Walk Funct
import random


def sailorwalk():
    nsteps = int(input('How many steps is the sailor going to take? '))
    pos = 0                                     # initial position of sailor    
    for z in range(0, nsteps+1):
    
        FwdOrBack = random.choice([1,2])        #1 = fwd 2 = back
        
        if FwdOrBack == 1:
            pos = pos + 1
       
        else:
            pos = pos - 1
        #print(pos)
    return 'The final position is '+str(pos)


#matlab version       
#Endpos = 0;
#    for k = 1:amountofsteps
#        Startpos = 0 + Endpos; %starting position of 0
#
#        Move = [-1 1]   ;
#        Step = Move(randi(numel(Move)));%move +1 or -1
#
#        Endpos = Startpos + Step;  % Adding +-1 to current post
#    end
#end

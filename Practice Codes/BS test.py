# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:11:22 2018

@author: Nick
"""
import random
import numpy as np
np.set_printoptions(threshold=np.inf)           #shows entire array. does not have ... in it
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from math import *
from scipy.stats import norm


def main():
    """
    this function sets up the matrix and has 
    increment values for the Y and X axis
    """
    ans             = '10 20' #input('Lower and upper stock prices you are examining? ')
    ans_split       = [float(n) for n in ans.split(' ' )]                     #[lower, upper]
    stock_increment = 4 #input('How many increments? ')
    
    stock_array    = np.linspace(ans_split[0], ans_split[1], stock_increment)

    ans_1           = '10 20' #input('Lower and upper volatilities you are examining (%)? ')
    ans_split1      = [float(n) for n in ans_1.split(' ' )]                     #[lower, upper]
    vol_increment   = 4 #input('How many increments? ')
        
    vol_array       = np.linspace(ans_split1[0], ans_split1[1], vol_increment)
    
    matrix = matrix_maker(len(stock_array),len(vol_array))
    
    final = put_shit_in_matrix(stock_array, vol_array, matrix)
    print(final)
    return plotter(final, stock_array, vol_array, stock_increment, vol_increment)
    
def matrix_maker(yaxis, xaxis):
    """
    creates the matrix of 0's y by x
    """
    
    matrix = np.zeros((yaxis,xaxis))                        #creates a matrix
    
    
    return matrix

def put_shit_in_matrix(stock_list, volatility_list, matrix):
    """
    uses the values in stock_list and volatility_list to calulate the respective 
    option premium
    """
    
    for i in range(len(stock_list)):            #array of stock prices
        for n in range(len(volatility_list)):   #array of volatilities
            #print(matrix)
            matrix[i][n] = BlackScholes_1(stock_list[i], volatility_list[n])
            #puts the black scholes value in the matrix
            #print(matrix)
            
    return matrix    
        
""" # The Black Scholes Formula
# CallPutFlag - This is set to 'c' for call option, anything else for put
# S - Stock price
# K - Strike price
# T - Time to maturity
# r - Riskfree interest rate
# d - Dividend yield
# v - Volatility
"""
def BlackScholes_1(S, v):
    """
    this function calculates the option 
    premium given a spot and vol value
    """
    CallPutFlag = 'c'
#    S = 196.2       #spot price
    K = 196         #strike prive
    T = 14/365      #time to maturity
    r = .02         #risk free rate
    d = .03         #dividend yield
#    v = .13         #percentage as decimal
    
    print('new run')
    print(S)
    print(v)
    
    d1 = (log(float(S)/K)+((r-d)+v*v/2.)*T)/(v*sqrt(T))
    d2 = d1-v*sqrt(T)
    if CallPutFlag=='c':
        return S*norm.cdf(d1)-K*exp((r-d)*T)*norm.cdf(d2)
    else:
        return K*exp(-r*T)*norm.cdf(-d2)-S*exp(-d*T)*norm.cdf(-d1)

def plotter(matrix, y_label, x_label, yincre, xincre):
    """
    pain in ass function that formats the graph
    """
    fig, ax = plt.subplots()

   
    print(x_label)    
    print(y_label)
    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            plt.text(x, y, '%4f' %matrix[y,x], horizontalalignment='center', verticalalignment='center',color='w')
    

    extent = (min(x_label), max(x_label), min(y_label), max(y_label))
      
    right_aspect = ((max(x_label)-min(x_label))/int(xincre)/((max(y_label)-min(y_label))/int(yincre)))
    #sets the right aspect ratio for the graph. since the Y and X axis are 
    #weird numbers it gets wonky and this fixes it
    ###Ensure that each cell in the graph is looks like a square
     

    #function below should display the respective cell value but it doesn't work with when
    #extent is used in the ax.imshow() function              
    
    
    
    
    plt.ylabel('Stock Price ($)')
    plt.xlabel('Volatility (as decimal)')
#    fig.colorbar(im)
    
    
    #ax.autoscale(tight=True)
    #ax.set_aspect('equal')
    
    ax.imshow(matrix)# , extent=extent, aspect = right_aspect)
    
#    for i in range(len(y_label)):
#        for j in range(len(x_label)):
#            text = ax.text(j,i, matrix[i, j], ha='center', va='center') #, color='b')
    
    
    
    
main()

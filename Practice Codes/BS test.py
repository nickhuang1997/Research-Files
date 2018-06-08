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
    uses all helper functions to run program
    takes the following inputs...
    1) Spot price range and step value
    2) Volatility range
    3) Strike price 
    4) Risk free rate
    5) Dividend Yield
    6) Days left until expiry
    7) 
    """
    ans             = '150 200'                             #input('Lower and upper stock prices you are examining? ')
    ans_split       = [float(n) for n in ans.split(' ' )]   #[lower, upper]
    stock_increment = 10 #int(input('How many increments for stock price? '))
    
    stock_array     = np.linspace(ans_split[0], ans_split[1], stock_increment)
    stock_array     = stock_array.round(decimals=2)             #rounds the array to 2 decimals. 
    
    ans_1           = '8 10' #input('Lower and upper volatilities you are examining (%)? ')
    ans_split1      = [float(n) for n in ans_1.split(' ' )] #[lower, upper]
    vol_increment   = 10 #int(input('How many increments for vol? '))
        
    vol_array       = np.linspace(ans_split1[0], ans_split1[1], vol_increment)
    vol_array       = vol_array.round(decimals=2)                 #rounds the array to 2 decimals. 
    
    matrix = matrix_maker(len(stock_array),len(vol_array))
    
    strikeprice     = float(input('What is the strike price? '))
    TimeToMat       = float(input('How long until expiration? (days) '))
    rfr             = float(input('What is the risk free rate? (as decimal) '))
    divY            = float(input('What is the divident yield? (as decimal) '))
    
    complete_matrix = put_shit_in_matrix(stock_array, vol_array, matrix, 
                                         strikeprice, TimeToMat, rfr, divY)
    # S, v, K, T, r, D
    
    print(complete_matrix)
    print(vol_array)
    print(stock_array)
    
    return plotter(complete_matrix, stock_array, vol_array, stock_increment, vol_increment)
    
def matrix_maker(yaxis, xaxis):
    """
    creates the matrix of 0's y by x
    """
    
    matrix = np.zeros((yaxis,xaxis))                        #creates a matrix
    
    
    return matrix

def put_shit_in_matrix(stock_list, volatility_list, matrix, strike, TimeToMat, rfr, divY):
    """
    uses the values in stock_list and volatility_list to calulate the respective 
    option premium
    """
    
    for i in range(len(stock_list)):                        #array of stock prices
        for n in range(len(volatility_list)):               #array of volatilities
            matrix[i][n] = BlackScholes_1(stock_list[i], (volatility_list[n]/100), 
                  strike, TimeToMat, rfr, divY) #need to divide by 100 bc given as %
            # S, v, K, T, r, D
            
            #puts the black scholes value in the matrix
    return matrix    
        
def BlackScholes_1(S, v, K, T, r, d):
    """
    this function calculates the option 
    premium given a spot and vol value
    
    # The Black Scholes Formula
# CallPutFlag - This is set to 'c' for call option, anything else for put
# S - Stock price
# K - Strike price
# T - Time to maturity
# r - Riskfree interest rate
# d - Dividend yield
# v - Volatility
    """
    CallPutFlag = 'c'
#    S = 196.2       #spot price
#    K = 196         #strike prive
#    T = 14/365      #time to maturity
#    r = .02         #risk free rate
#    d = .03         #dividend yield
#    v = .13         #percentage as decimal
    
#    print('new run')
#    print(S)
#    print(v)
    T = T/365                   #Black Scholes formula takes T as % of a year
    
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
    fig, ax = plt.subplots(figsize=(20,10))#(figsize=(width,height))

    heatmap = ax.pcolor(matrix)
#                        edgecolors='w')  # put white lines between squares in heatmap
    data = matrix
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            plt.text(x + 0.5, y +0.5, '%.2f' % data[y, x], #data[y,x] +0.05 , data[y,x] + 0.05
                 horizontalalignment='center',
                 verticalalignment='center')

    ax.autoscale(tight=True)  # get rid of whitespace in margins of heatmap
    ax.set_aspect('equal')  # ensure heatmap cells are square

#if you want to take out tick marks, uncomment below
#    ax.tick_params(bottom='off', top='off', left='off', right='off')  # turn off ticks
    cbar = fig.colorbar(heatmap)   
    cbar.ax.set_ylabel('Option Premia ($)', size = 15, labelpad = 20, rotation=270)
    
#must put colorbar before the set_ticks otherwise it will 
#not show up (suspect that set_ticks overwrites the colorbar)
    ax.set_yticks(np.arange(len(y_label)) + 0.5)
    ax.set_yticklabels(y_label, size=15)
       
    ax.set_xticks(np.arange(len(x_label)) + 0.5)
    ax.set_xticklabels(x_label, size=15)
#    ax.xaxis.set_major_formatter(format_pct())
    plt.ylabel('Stock Price ($)',size = 15)
    plt.xlabel('Volatility (%)',size = 15)
       
main()

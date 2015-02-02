#!/usr/bin/env python

import numpy as np
from math import floor

def check_index(index, simulation,n):
    '''
    '''
    
    if simulation[index]==0:
        if index==0:
            if (simulation[0]==simulation[1]):
                return True 
        elif index==n-1:
            if (simulation[n-1]==simulation[n-2]):
                return True
        else:
            if (simulation[index-1]==simulation[index+1])\
            and simulation[index-1]==0:
                return True 
    else:
        return False 

def main(n, iterations, percent=.35):

    np.random.seed(86)

    occupied=[]
    
    while len(occupied)< iterations:
        
        i=0
        simulation=np.array([0]*n)
        
        while i<floor(n*percent):
            index=np.random.randint(0,n)
            if check_index(index, simulation,n):
                i=i+1
                simulation[index]=1
                
        index=np.random.randint(0,n)
        
        for i in range(index,-1,-1):
            if check_index(i, simulation,n):
                simulation[i]=1
        for i in range(index,n):
            if check_index(i, simulation,n):
                simulation[i]=1
                
        occupied.append(float(simulation.sum())\
                                 /float(n))
        print "%i interation(s) remain"\
               %(iterations-len(occupied))
                
    
    occupied=np.array(occupied)
    
    print "N=%i mean=%.14f std=%.14f" %(n,occupied.mean(),\
                                        occupied.std())
    
    return None 
                

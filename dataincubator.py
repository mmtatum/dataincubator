#!/usr/bin/env python

import numpy as np

def check_simulation(simulation,n):
    for i,j in enumerate(simulation):
        if i==0:
            if j!=simulation[i+1]:
                continue 
            else:
                break
        elif i==n-1:
            if j!=simulation[i-1]:
                return True  
            else:
                break 
        else:
            if (j==simulation[i-1] or j==simulation[i+1])\
            and j==1:
                    break
            elif (j==simulation[i-1] and j==simulation[i+1])\
            and j==0:
                break
            else:
                continue 
    
    return False

def main(n, times):

    np.random.seed(86)

    occupied=[]
    
    while len(occupied)< times:
        
        simulation=np.random.randint(0,2,n)
        if simulation.sum() < n/3 :#or simulation.sum() > n/2+1:
            continue
        else:
            check= check_simulation(simulation,n)
            if check:
                
                occupied.append(float(simulation.sum())\
                                 /float(n))
                #print "%i interation(s) remain"\
                #%(times-len(occupied))
                
    
    occupied=np.array(occupied)
    
    print " main N=%i mean=%.11f std=%.11f" %(n,occupied.mean(),\
                                        occupied.std())
    return None 

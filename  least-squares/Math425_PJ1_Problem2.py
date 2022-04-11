#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 08:55:09 2021

@author: nianziyi
"""

import numpy as np

###a
T = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
Y = np.array([0, 8.8, 29.9, 62.0, 104.7, 159.1, 222.0, 294.5, 380.4, 471.1,
              571.7, 686.8, 809.2])
    
Beta = np.polyfit(T, Y, 3) #find the coeficient of y
print("(a)the least-squares cubic curve y = β3t^3 + β2t^2+ β1t+ β0 is") 
print(np.poly1d(Beta))#find the least-square cubic curve
print()

###b
velocity_curve = np.polyder(Beta) #take derivative of y,find v function
velocity = np.polyval(velocity_curve, 4.5) #find the value of v when t=4.5
print("(b)velocity when t = 4.5 is", velocity)
print()

###c
w = np.array([1,1,1,0.9,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1])
w = np.diag(w)
weighted_T = np.dot(w,T)
weighted_Y = np.dot(w,Y)
weighted_Beta = np.polyfit(weighted_T, weighted_Y, 3)
weighted_velocity_curve = np.polyder(weighted_Beta) #take derivative of y,find v function
weighted_velocity = np.polyval(weighted_velocity_curve, 4.5)

print("(c)the least-squares cubic curve after applying weighting matrix is")
print(np.poly1d(weighted_Beta))#find the least-square cubic curve
print()
print("velocity when t = 4.5 is", weighted_velocity)


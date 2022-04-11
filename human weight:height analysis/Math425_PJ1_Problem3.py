#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 06:24:22 2021

@author: nianziyi
"""

import numpy as np
from matplotlib import pyplot as plt

file = 'height_weight_clean.txt'
data = np.loadtxt(file) 

###(a)
#split into 3 data sets
training_set = data[0:15000,:]  #training_set:1-15000
validation_set = data[15000:23000,:] #validation_set:15001-23000
test_set = data[23000:25000,:] #test_set:23001-25000

#scatter plot
training_set_height = training_set[:,1]  #take height as x
training_set_weight = training_set[:,2]  #take weight as y

fig,ax = plt.subplots()

ax.scatter(training_set_height, training_set_weight,
           c = 'b', marker = 'x', label = 'Training Set :' )
ax.legend()
ax.set(xlabel = 'height(inches)', ylabel = 'weight(pounds)')
plt.show()


###(b)
def gradientDescent(x, y, alpha, iters, theta0, theta1):
    n = len(x) # number of points
    #x = x.reshape(n,1)
    #y = y.reshape(n,1)
    
    for i in range(iters):
        y_pred = theta0 + theta1 * x #predicted value of y
        
        D_theta0 = (1/n) * sum(y_pred - y) #derivative of theta0
        D_theta1 = (1/n) * sum(x * (y_pred - y)) #derivative of theta1
        
        theta0 = theta0 - alpha * D_theta0
        theta1 = theta1 - alpha * D_theta1 #update theta0 and theta1 simultaneously
        
    return theta0, theta1


theta0 = 0 
theta1 = 0   #y = theta0 + theta1 * x
alpha = 0.01 # learning rate
iters = 100 #iteration times
x = validation_set[:,1]  #take height as x
y = validation_set[:,2]  #take weight as y
    
#call the function gradientDescent
theta0, theta1 = gradientDescent(x, y, alpha, iters, theta0, theta1)
print(theta0, theta1)
    

#y_hat = theta0 + theta1 * x #predicted value of y

#plt.scatter(x, y, c = 'b', marker = 'x', label = 'H: inches, W: pounds') 
#ax.legend()
#ax.set(xlabel = 'height', ylabel = 'weight')
#plt.plot(x, y_hat, c = 'r')
#plt.show()


###(d)
A = data[:,1] #height
A = A.reshape(25000,1)
#A = np.insert(A,0,1,1)
y = data[:,2] #weight
Q,R = np.linalg.qr(A) #find Q and R
R_inv = np.linalg.inv(R)
theta = np.dot(R_inv, np.dot(Q.T,y))
print(theta)
print('least-squares linear model is: ')
print('weight =', theta[0], '* height')
#print('weight =', theta[0],'+',theta[1], '* height')

        
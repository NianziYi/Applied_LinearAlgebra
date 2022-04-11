#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:38:54 2021

@author: nianziyi
"""

import numpy as np
from matplotlib import pyplot as plt

data = np.load("bird.npy")

###a.i create the first tile
H3_i = np.array([[1, 0, 0.712],
                 [0, 1, 0.432],
                 [0, 0, 1]])
H2_i = np.array([[np.cos(np.pi), -np.sin(np.pi), 0], 
                 [np.sin(np.pi), np.cos(np.pi), 0],
                 [0, 0, 1]])
H1_i = np.array([[1, 0, -0.712],
                 [0, 1, -0.432],
                 [0, 0, 1]])

#H_i is the transformation matrix for rotation through pi about (0.712,0.432)
H_i = np.dot(H3_i, (np.dot(H2_i,H1_i))) 
print('transformation matix for a.i is')
print(H_i)
print()


###a.ii create the second tile
#transformation matrix for reflection through y=0.618
H1_ii = np.array([[1, 0, 0],
                  [0, -1, 1.236],
                  [0, 0, 1]]) 
#transformation matrix for translation by 0.4084 along x-axis
H2_ii = np.array([[1, 0, 0.4084], 
                  [0, 1, 0],
                  [0, 0, 1]])
#multiply H1_ii,H2_ii to get final transformation matrix
H_ii = np.dot(H2_ii, H1_ii) 
print('transformation matix for a.ii is')
print(H_ii)
print()


###a.iii create third tile
#transformation matrix for reflection through x=0.5078
H1_iii = np.array([[-1, 0, 1.0156],
                   [0, 1, 0],
                   [0, 0, 1]])
#transformation matrix for translation by 0.1 along y-axis
H2_iii = np.array([[1, 0, 0],
                   [0, 1, 0.1],
                   [0, 0, 1]])
#multiply H1_iii,H2_iii to get final transformation matrix
H_iii = np.dot(H2_iii, H1_iii) 
print('transformation matix for a.iii is')
print(H_iii) 
print()
        

###a.iv create forth tile 
#transformation matrix for translation by 0.4720 along y-axis
H_iv = np.array([[1, 0, 0],
                 [0, 1, 0.472],
                 [0, 0, 1]]) 
print('transformation matix for a.iv is')
print(H_iv)


###a.v
#1.create four (3x11)array by applying four transformation matrix to original data
#2.plot data1,2,3,4 together

def apply_transformation(original_data, trans_matrix ):
    new_data = np.insert(original_data,2,1,0) #insert a row with value of 1 to make it be 3x11
    for i in range(11):                      #update each point in original data
        temp = new_data[:,i]
        new_point = np.dot(trans_matrix,temp)
        new_data[:,i] = new_point
    plt.plot(new_data[0], new_data[1], 'k-') #plot new data
    return new_data

#get 4 new datasets by applying corresponding transformation matrix to original data
data1 = apply_transformation(data, H_i) 
data2 = apply_transformation(data, H_ii)
data3 = apply_transformation(data, H_iii)
data4 = apply_transformation(data, H_iv)


###b
class Transformations:
    def __init__(self,data):
        self.x = data[0]
        self.y = data[1]
        
    def display(self,color):
        plt.plot(self.x, self.y, 'k-', c = color)
        plt.show
        
    def translate(self,a,b):
        self.x  = self.x + a
        self.y  = self.y + b
        
#translate each small tile 3 times through(0,0.7441*n)
#n = 1,2,3 
def translate_data (data, color): 
    for n in range(0,4):
        plot = Transformations(data)
        plot.translate(0, 0.7441 * n)
        plot.display(color)

translate_data(data1,'red')    #translate data1 3 times
translate_data(data2,'green')  #translate data2 3 times
translate_data(data3,'blue')   #translate data3 3 times
translate_data(data4,'yellow') #translate data4 3 times
    

###c
#repeat partb, translate each small tile 3*5 times through(-0.8168*n1,0.7441*n2)
#n1 = 1,2,3; n2 = 1,2,3,4,5
def translate_data_final (data,color):
    for n1 in range(0,4):
        for n2 in range(0,6):
            plot = Transformations(data)
            plot.translate(-0.8168 * n2, 0.7441 * n1)
            plot.display(color)
            
translate_data_final(data1,'green')
translate_data_final(data2,'yellow')
translate_data_final(data3,'blue')
translate_data_final(data4,'red')







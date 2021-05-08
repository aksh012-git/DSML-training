# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:12:06 2021

@author: Aksh
"""


import numpy as np

#1d []
#2d [ [1d] , [1d] , [1d] ]
#3d [ [2d] , [2d] , [2d] ]

a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a.ndim)
print(a)
print(a[0,1,1]) #0th row of 3d array and in this array 1th row and in this array 1st element
print(a[:,1,:])
print(a[:,:,0])
print(a[:,0,0])

print("----------------------------------------------------------")
x = np.array([[[1,2],[3,4]],[[5,6],[7]]])
print(x)

#you want to print 1 in x array then you perform x[0,0,0] but this is not right bcz bcz at that time list in array
#so you print this
print(x[0,0][0])

print("----------------------------------------------------------")
y = np.array([[[1,2],[3,4]],[[5,6]],[[7,8],[9],[10]]])
print(y)
print(y[0])
#you may find [1,2] than you don't use print(y[0,0]) 
print(y[0][0])
print(y[2][1][0])



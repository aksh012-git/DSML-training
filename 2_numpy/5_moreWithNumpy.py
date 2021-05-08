# -*- coding: utf-8 -*-
"""
Created on Sun May  2 00:36:39 2021

@author: Aksh
"""

import numpy as np


print(np.zeros((2,3))) #2d matrix
print(np.zeros(5)) #1d 
print(np.zeros((3,2,2))) #3d  
print(np.zeros((3,4,3)))
print(np.zeros((5,2,2)))


print("-------------------")

print(np.ones((2,2,2)))

print("-------------------")

print(np.full((2,3,3),12,dtype='int32'))

print("---------------------")

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
x = np.full_like(a,3)
print(x)

print("---------------------")

#tdentity matrix ---> all diagonal are 1
print(np.identity(4,dtype='int32'))
print(np.eye(3)) #you can same things

print("---------------------")

#reshape of array 
q = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(q)

l = q.reshape((5,2)) #reshape with 2d
print(l)

j = q.reshape((2,1,5)) #reshape with 3d
print(j)

print(q.reshape((10))) #reshape with 1d

print("----------------------")
r = np.array([[1,2,3,4],[5,6,7,8]])
print(r.reshape((8)))
print(r.reshape((4,2)))
print(r.reshape((2,4)))
print(r.reshape((2,2,2)))
print(r.reshape((4,1,2)))

print("----------------------")

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

#vertically stackd array
print(np.vstack([v1,v1,v2,v2]))

#horizontally stack array
print(np.hstack([v1,v2,v1]))















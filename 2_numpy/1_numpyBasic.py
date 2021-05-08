# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 18:08:30 2021

@author: Aksh
"""


import numpy as np

#this is list
x = [1,2,3,4]
print(x)

#convert list to numpy array
w = np.array(x)
print(w)

a = [1,2,3,4]
b = [4,3,2,1]

# you can perform a*b than error: "" can't multiply sequence by non-int of type 'list' ""
#print(a*b)


n = np.array(a)
m = np.array(b)
print(n*m)


#q1 becom a int type
q1 = np.array([1,2,3,4])
print(q1)
#q2 become a flote type
q2 = np.array([1,2,3.2])
print(q2)
#q3 become a string type
q3 = np.array([1,2.3,'aksh'])
print(q3)
#because, array is collection of same data type

#find dimension of np array
print(q1.ndim)
#find shap --- shap means how many column and row (column,row)
print(q1.shape)
#find type
print(q1.dtype)
#find itemsize each item size in byts
print(q1.itemsize)
#find sum of itemsize
print(q1.nbytes)


q4 = np.array([1,2,3,4],dtype='int16')
print(q4.dtype)
print(q4.itemsize)
print(q4.nbytes)














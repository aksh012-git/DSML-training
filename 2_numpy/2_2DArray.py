# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 23:43:07 2021

@author: Aksh
"""

#2d numpy

import numpy as np

a = np.array([[1,3,2,3],[1,2,2,3]])

print(a.ndim)
#shap ---> (column,row)
print(a.shape)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)


b = np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
print(b)
print(b[0,4:6]) #0th row and 4 to 6th column
print(b[:,3:7]) #all row with 3 to 7th column
print(b[1,5])


#you can read right to left and rigth side start 1 to n and left side start 0 to n
print(b[1,-5])
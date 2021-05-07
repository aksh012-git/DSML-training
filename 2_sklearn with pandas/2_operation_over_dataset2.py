# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:19:51 2021

@author: Aksh
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer

#------------------------------------------------------------------------------------------------------------
#conver categorical data to numerical data using OneHotEncoder
dataset2 = pd.read_csv('dataset2.csv')
x = dataset2.iloc[:,:].values
print(x)

#------------------------------------------------------------------------------------------------------------
#ColumnTransformer([("any string you write",define encoder,define column)],remainder='passthrough')
#you not write remainder='passthrough' then copy x only defined column
#without remainder
transform = ColumnTransformer([("aksh",OneHotEncoder(),[0])])
x1 = transform.fit_transform(x)
print(x1)


#------------------------------------------------------------------------------------------------------------
transform = ColumnTransformer([("aksh",OneHotEncoder(),[0])], remainder='passthrough')
x2 = transform.fit_transform(x)
print(x2)


#------------------------------------------------------------------------------------------------------------
"""
Overcast- O is first in A to Z
Rain - R is after O
Sunny - S is after R

Overcast  Rain   Sunny   
  1        0       0
  0        1       0
  0        0       1
  
  [1 0 0] for Overcast
  [0 1 0] for Rain
  [0 0 1]for Sunny
  
"""


#------------------------------------------------------------------------------------------------------------
#use OneHotEncoder with 4th column
transform = ColumnTransformer([("aksh",OneHotEncoder(),[4])], remainder='passthrough')
x3 = transform.fit_transform(x2)
print(x3)


#------------------------------------------------------------------------------------------------------------
#use OneHotEncoder with 6th column
transform = ColumnTransformer([("aksh",OneHotEncoder(),[6])], remainder='passthrough')
x4 = transform.fit_transform(x3)
print(x4.astype(int))


#------------------------------------------------------------------------------------------------------------
"""
1   2    3    4    5
1   0    0    0    0
0   1    0    0    0
0   0    1    0    0
0   0    0    1    0
0   0    0    0    1
"""

#see your data is [1 0 0 0 0 0 0 1 0 0 1] than first five column is x3 and than 3 column is x2 than 3 column is x2








# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:24:55 2021

@author: Aksh
"""

#--------------------------------------------------------------------------------------------------------
#Linear Algebra using python
"""
our equation
x + 3y + 10z = 10
2x + 12y + 7z = 18
5x + 8y + 8z = 30
"""


import numpy as np
from scipy import linalg
#SciPy stands for Scientific Python

x = np.array([[1,3,10],[2,12,7],[5,8,8]])

y = np.array([[10],[18],[30]])

# x.z = y
z = linalg.solve(x,y)
print(z)

#x.z - y = 0
print(x.dot(z) - y)

#--------------------------------------------------------------------------------------------------------
#you can also make array using scipy but warring is there
import scipy as sc
m = sc.array([[1,2,3],[4,5,6]])
print(m)


#--------------------------------------------------------------------------------------------------------
#determinant of given matrix 2 x 2
x1 = np.array([[1,2],[3,4]])

y1 = linalg.det(x1)


#determinant of given matrix 3 x 3
x1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

y1 = linalg.det(x1)


#--------------------------------------------------------------------------------------------------------
#Eigen Value and Eigen Vector
"""
|A - λI| = 0
A = your matrix
I = identity metrix
"""
x = np.array([[-6,3],[4,5]])

y = linalg.eig(x)


#--------------------------------------------------------------------------------------------------------
#Linear regression
x = [1,2,3,4,5,6]
y = [2,4,6,8,10,12]

"""
y = mx + c 
m = slope
c = intercept of y

rvalue = Correlation coefficient(how many close your value in linear line)
         rvalue is 1 then your value fitted on your liner line
         
pvalue = Two-sided p-value for a hypothesis test whose null hypothesis is that the slope is zero, 
         using Wald Test with t-distribution of the test statistic.
         
stderr = Standard error is average between your linear line to your point.

follow this link- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
"""

from scipy.stats import linregress

slope,intercept,r_value,p_value,stderr = linregress(x,y)


#--------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

plt.plot(x,y,'o',label="my data plot for regression")

#x is our list
#convert x to array
x = np.array(x)
#y = mx + c
y = (slope*x) + intercept

plt.plot(x,y,'r',label="line fitter after regression")
#for show your label
plt.legend()
plt.savefig("mydata.png")


#--------------------------------------------------------------------------------------------------------
x = np.random.random(10)
y = np.random.random(10)

slope,intercept,r_value,p_value,stderr = linregress(x,y)

import matplotlib.pyplot as plt

plt.plot(x,y,'o',label="my data plot for regression")

#x is our list
#convert x to array
x = np.array(x)
#y = mx + c
y = (slope*x) + intercept

plt.plot(x,y,'r',label="line fitter after regression")
#for show your label
plt.legend()
plt.savefig("mydataRandom.png")


#--------------------------------------------------------------------------------------------------------
#you are having a dataset
#How good your dataset?
# chack Goodness of fit analysis 

#np.random.normal(mean,standard deviation,how many value you need)
x = np.random.normal(50,2,500)

#histogram graph of our x dataset
plt.hist(x)
plt.savefig("mydataHistogram")

#see graph mean value is 50
# most off standard deviation is 2
x.std()


#--------------------------------------------------------------------------------------------------------
#Gaussian Distribution
from scipy.stats.kde import gaussian_kde
#gaussian_kde(dataset)
kde_x = gaussian_kde(x)

#kde_x(points)
plt.plot(x,kde_x(x))
plt.savefig("gaussian.png")
#see graph is vary tough for understanding


#--------------------------------------------------------------------------------------------------------
#so i put linear space for make easy understanding
from numpy import linspace
#linspace(start, stop,how many value between start to stop)
linspace_x = linspace(min(x), max(x),100)

plt.plot(linspace_x,kde_x(linspace_x))
plt.savefig("gaussian-linspace.png")














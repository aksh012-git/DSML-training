# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:37:42 2021

@author: Aksh
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

#--------------------------------------------------------------------------------------------------------------------
dataset = pd.read_csv("Social_Network_Ads.csv")
x = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,-1].values

#--------------------------------------------------------------------------------------------------------------------
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)

#--------------------------------------------------------------------------------------------------------------------
#in data set vary big value and vary small value availabe so use SC
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

#--------------------------------------------------------------------------------------------------------------------
#apply SVM
"""
learn about SVM follow link --
1)https://www.youtube.com/watch?v=xLkk6MUrvrw
2)https://www.youtube.com/watch?v=0MJTaPoHv-g
"""
from sklearn.svm import SVC

"""
kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’}, default=’rbf’
Specifies the kernel type to be used in the algorithm.
 It must be one of ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ or a callable.
 If none is given, ‘rbf’ will be used.
"""

#change 'kernal' value and chack accuracy 
classifire = SVC(kernel = 'rbf',random_state=0)
classifire.fit(x_train,y_train)

#--------------------------------------------------------------------------------------------------------------------
y_pred = classifire.predict(x_test)


#--------------------------------------------------------------------------------------------------------------------
#makking the confusion matrix to find accuracy
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#--------------------------------------------------------------------------------------------------------------------
#see accuracy
print((cm[0][0])+cm[1][1]/(cm[0][0] +cm[1][1]+cm[1][0]+cm[0][1])*100)

#performance measurement report using 'classification_report'
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#--------------------------------------------------------------------------------------------------------------------
"""
chack more accuracy and use other model
-naive bayes
-Decision Tree
-Random Forest

-convert in your dataset Social_Network_Ads.csv 'Gender' to numerical data then chack acuuracy
"""
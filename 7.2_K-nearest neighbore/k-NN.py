# -*- coding: utf-8 -*-
"""
Created on Wed May 26 09:20:07 2021

@author: Aksh
"""


#for learn K-nearest neighbore --->>https://www.youtube.com/watch?v=CJjSPCslxqQ

#--------------------------------------------------------------------------------------------------------------------
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
#apply k-NN
from sklearn.neighbors import KNeighborsClassifier
#KNeighborsClassifier('how many neighbors you choose', 'use for find distance', 
#                                     if p=1 this define 'manhattan_distance' and p=2 then define euclidean_distance)
classifire = KNeighborsClassifier(n_neighbors = 5,metric = "minkowski",p=2)
classifire.fit(x_train,y_train)

#--------------------------------------------------------------------------------------------------------------------
#predicting the test set resulte
y_pred = classifire.predict(x_test)

#--------------------------------------------------------------------------------------------------------------------
#makking the confusion matrix to find accuracy
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#see accuracy
print((cm[0][0])+cm[1][1]/(cm[0][0] +cm[1][1]+cm[1][0]+cm[0][1])*100)

#--------------------------------------------------------------------------------------------------------------------
#performance measurement report using 'classification_report'
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#--------------------------------------------------------------------------------------------------------------------
"""
---------- see more about and serch in google GridSearchCV---------------------
from sklearn.model_selection import GridSearchCV

grid_params = {
        'n_neighbors':[3,5,11,19],
        'weights':['uniform','distance'],
        'metric': ['euclidean','manhattan']
    }


gs = GridSearchCV(KNeighborsClassifier(),grid_params,verbose=1,cv=3,n_jobs=-1)

gs_result = gs.fit(x_train, y_train)

y_pred = gs.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#see accuracy
print((cm[0][0])+cm[1][1]/(cm[0][0] +cm[1][1]+cm[1][0]+cm[0][1])*100)

see - https://medium.com/@erikgreenj/k-neighbors-classifier-with-gridsearchcv-basics-3c445ddeb657
"""




    














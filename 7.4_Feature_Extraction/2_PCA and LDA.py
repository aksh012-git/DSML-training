# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:44:04 2021

@author: Aksh
"""

"""
using Feature Extraction --->>
you can solve this problem:
    -how graphical Representation in 3D
    -Model Overfitting
    -Highly Correlated Attributes
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

dataset = pd.read_csv("wine.csv")

#--------------------------------------------------------------------------------------------------------------------
#see correlation metrix of our datset
corelationMatrix = dataset.corr()
print(corelationMatrix)

#correlation Matrix see ,which column how many related each other
#in this matrix =1 is vary correlated and <=0 is very less correlated

#--------------------------------------------------------------------------------------------------------------------
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)


#--------------------------------------------------------------------------------------------------------------------
#in data set vary big value and vary small value availabe so use SC
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

#--------------------------------------------------------------------------------------------------------------------
#apply PCA
from sklearn.decomposition import PCA
#n_components=2 means our 13 column convert 2 column , you can use also other number and generet column
pca = PCA(n_components=2)
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)

#--------------------------------------------------------------------------------------------------------------------
#apply logistic regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(random_state=0)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

#--------------------------------------------------------------------------------------------------------------------
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)





#------------------------------------------ LDA ---------------------------------------------------------------------
#moving with second Extraction technique LDA 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis(n_components=2)

x_train = lda.fit_transform(x_train,y_train)
x_test = lda.transform(x_test)

#--------------------------------------------------------------------------------------------------------------------
#apply logistic regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(random_state=0)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

#--------------------------------------------------------------------------------------------------------------------
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)





#you apply PCA then you not taking y_train in fit_transfrom, you take only x_train
#means you not take output column only take input column
#then PCA called "unsupervised" dimensionality reduction feature extraction technique


#you apply LDA then you use x_train and y_train also in fit_transfrom.
#means you take output and input column
#then LDA called "supervised" dimensionality reduction feature extraction technique 




# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:52:37 2021

@author: Aksh
"""

"""


Types of Boosting Algorithms
1. AdaBoost (Adaptive Boosting)
2. Gradient Tree Boosting
3. XGBoost
"""

import pandas as pd
dataset = pd.read_csv('data.csv')

#-------------------------------------------------------------------------------------------------------------
#split into input and output
x = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1]

#-------------------------------------------------------------------------------------------------------------
#split into traning and testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

#-------------------------------------------------------------------------------------------------------------
#add boosting algorithms AdaBoost variant
from sklearn.ensemble import AdaBoostClassifier
model = AdaBoostClassifier()

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

#-------------------------------------------------------------------------------------------------------------
#use confusion_matrix
from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
#cm define matrix of y_test and y_pred ,which place your actual value and predicted value is rigth or wrong


#-------------------------------------------------------------------------------------------------------------
#find our accuracy
print(((cm[0][0]+cm[1][1])/(cm[0][0]+cm[1][1]+cm[1][0]+cm[0][1]))*100)

#another way to find -- first import "from sklearn.metrics import confusion_matrix,accuracy_score"
accuracy_score(y_test, y_pred) * 100


#-------------------------------------------------------------------------------------------------------------







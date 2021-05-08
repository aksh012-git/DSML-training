# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:18:25 2021

@author: Aksh
"""


#multi linear regession
#Many input and one output
#y = m1x1 + m2x2 + ..... + c

#----------------------------------------------------------------------------------------------------------
import pandas as pd
dataset4 = pd.read_csv('dataset4.csv')
dataset4.head()

#see our datset4 and this datset4 one state line is categorical data

#----------------------------------------------------------------------------------------------------------
x = dataset4.iloc[:,:-1].values
y = dataset4.iloc[:,-1].values

#----------------------------------------------------------------------------------------------------------
# x is our input
x

#----------------------------------------------------------------------------------------------------------
# y is our output
y

#----------------------------------------------------------------------------------------------------------
#change categorical data to numerical dat
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
transform = ColumnTransformer([("aksh",OneHotEncoder(),[3])], remainder='passthrough')
x = transform.fit_transform(x)
x

#----------------------------------------------------------------------------------------------------------
#spliting datset3 into traing and testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=1/3,random_state=0)


#----------------------------------------------------------------------------------------------------------
#for multi linear regression
from sklearn.linear_model import LinearRegression

#make machine learning model
regeressor = LinearRegression()
#ML model is empty at that time 

#you want to train your ML model than fit 
regeressor.fit(x_train,y_train)


#----------------------------------------------------------------------------------------------------------
#predicting the test result
y_pred = regeressor.predict(x_test)
y_pred

#see and  y_pred and y_test 

#----------------------------------------------------------------------------------------------------------
y_pred1 = regeressor.predict([[0.0, 1.0, 0.0, 66051.52, 182645.56, 118148.2]])
y_pred1


#----------------------------------------------------------------------------------------------------------
#you can seee your accuracy ,how well your dataset train or test
regeressor.score(x_train,y_train)
regeressor.score(x_test,y_test)


#----------------------------------------------------------------------------------------------------------
#how to save or dump your accuracy model 
#use library

import pickle
from sklearn.externals import joblib
#save your model in .plk file
#joblib.dump(model_name,'filename.pkl')
joblib.dump(regeressor,'2_myregressor.pkl')

#----------------------------------------------------------------------------------------------------------
#read or load pkl file
my_pkl_file = joblib.load('2_myregressor.pkl')


#----------------------------------------------------------------------------------------------------------
y_pred = my_pkl_file.predict(x_test)
y_pred
y_pred = my_pkl_file.predict(x_train)
y_pred
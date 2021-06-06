# -*- coding: utf-8 -*-
"""
Created on Sun May 30 10:55:09 2021

@author: Aksh
"""


"""
Neural Network

in "neuron" main 3 component-->>
1) Dendrites - this is a receiver 
2) axon - this is a transmitter
3) neuron - processor, neuran to process information received via dendrites

The use of neural networks is to make your computer as intelligent as your brain

in an artificial neural network 3 layers are there:
    1 - input layer
    2 - hidden layer
    3 - output layer

in output layer 2 functions are use 
1)sigmoid 
2)softmax
    
for hidden layer many function are use 
1 - Binary step 
2 - Liner 
3 - ReLU(rectifide liner unit)
4 - LeakyReLU
5 - Tanh
    
-in 90% cases use ReLU
"""

#--------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
bankdata = pd.read_csv("Churn_Modelling.csv") 

#in this dataset 0,1,2th column are meaning less

#--------------------------------------------------------------------------------------------------------------
x = bankdata.iloc[:,3:-1].values
y = bankdata.iloc[:,-1].values

#--------------------------------------------------------------------------------------------------------------
#see our x data 1st or 2nd column are categorical dataset
#so first i aplly one onehotEncoder to our 1st column

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer

transform = ColumnTransformer([("aksh",OneHotEncoder(),[1])],remainder='passthrough')
x = transform.fit_transform(x)

#see our x then 3 new column are genereted then 0th column are not important bcz i have 2 column so i remove this 0th column
x = x[:,1:]
  
#see our x and see 3rd column this is our categorical data so transform to numerical data
transform = ColumnTransformer([("aksh",OneHotEncoder(),[3])],remainder='passthrough')
x = transform.fit_transform(x)
#you also see , you make fit_transform then our converted numerical data is start 0th column
#and i also delete one column bcz male is 1 and female is 0 so generet 2 column 
#then delete one column bcz you also make great output 1 column in one column instead of two columns
x = x[:,1:]

#--------------------------------------------------------------------------------------------------------------

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

#--------------------------------------------------------------------------------------------------------------

#for some large value and some small value in our dataset
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#--------------------------------------------------------------------------------------------------------------

#let's create Artificial neural network
#import keras
from tensorflow import keras 


#--------------------------------------------------------------------------------------------------------------
#you want to add hidden layer horizontally so use Sequential
from tensorflow.keras.models import Sequential


#--------------------------------------------------------------------------------------------------------------
#you want to add neuron vertically in any hidden layer so use Dense
from tensorflow.keras.layers import Dense


#--------------------------------------------------------------------------------------------------------------
clasifire = Sequential()

#--------------------------------------------------------------------------------------------------------------
#in our x 11 column so how many neurons are add (11+1)/2 = 6 
#so in one hidden layer 6 neurons are there
clasifire.add(Dense(units=6,kernel_initializer='uniform',activation='relu',input_shape=(11,)))

clasifire.add(Dense(units=6,kernel_initializer='uniform',activation='relu'))

# our network is -->
# Input layer -> hidden layer 1 -> hidden layer 2 -> Output layer
# first hidden layer connected to input layer so you need to give a shape but second hidden layer connected to 1st hidden layer so not need to give shape 
#--------------------------------------------------------------------------------------------------------------

#add output layer 
# see activation='sigmoid' bcz this is a output function
clasifire.add(Dense(units=1,kernel_initializer='uniform',activation='sigmoid'))


#--------------------------------------------------------------------------------------------------------------
#compiling the ANN(Artificial neural network)
#add optimizer, many optimizer are available i use "adam"
clasifire.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#--------------------------------------------------------------------------------------------------------------
#fiting the ANN to the training dataset
#epochs=100 means our machine train our model 100 times
# batch_size=10 then our size of row in x_train 8000/10 = 800
#in one epochs 800 time train our model 
clasifire.fit(x_train,y_train,batch_size=10,epochs=100)


#--------------------------------------------------------------------------------------------------------------
y_pred = clasifire.predict(x_test)
y_pred = (y_pred > 0.5)

#--------------------------------------------------------------------------------------------------------------
#see accuuracy
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)


print((cm[0][0] + cm[1][1]) /(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1])*100 )

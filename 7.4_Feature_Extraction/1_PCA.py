# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:02:26 2021

@author: Aksh
"""

"""
i have a 5 different medicine of same disease than medicine number 1 and 2 is vary useful for me
and it's a give better acuuracy for me. other medicine not good for me this called "Over fitting Problem" 

same as our dataset some model are give a better acuuracy and some not.

-then what feature are the best for your dataset
find best feature than to technique are available
1) Feature selection
2) Feature Extraction

ex - you have 4 chocolate of diffrent brand and you chhose only one for you
-then you select any one chocolat this called "Feature selection"
-but you want to test all chocolate than you cut 25% part of all chocolate and make a new chocolate this called "Feature Extraction"

in "Feature selection" many technique are available - Forward feature selection, backward elimination, etc.

in "Feature Extraction" PCA(Principal component Analysis), LDA(Linear Discreminent analysis),kernel PCA etc.
"""

#--------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

dataset = pd.read_csv("wine.csv")

#our data is classification variant 

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
"""
whya use feature extraction-->>
Feature extraction helps to reduce the amount of redundant data from the data set. 
In the end, the reduction of the data helps to build the model with less machine's efforts 
and also increase the speed of learning and generalization steps in the machine learning process.

you can change n column to 2 then you can easily do plot your data

solve overfitting problem.
"""














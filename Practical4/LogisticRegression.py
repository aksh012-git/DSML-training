# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:46:12 2021

@author: Aksh
"""


"""
1)continuous set of values ---> in this dataset value is not a limited, Ex-> your of experience and salary 
2)discrete set of values ---> in this datset alue is limited output, Ex-> man purchase Audi car or not then only output 'Yes' or 'No'

-your value "Continuous set of value" then you can use "Regression"
-your value "discrete set of values" then you can use "Classification" 
"""
#----------------------------------------------------------------------------------------------------------
import pandas as pd

dataset = pd.read_csv('Social_Network_Ads.csv')
dataset.head()


#----------------------------------------------------------------------------------------------------------
#split data set into input and output 
#as of now i put column n. 2 and 3 as input and column no. 4 as output
x = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,4].values
x
y


#----------------------------------------------------------------------------------------------------------
#split my dataset into traing and tasting
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)



#----------------------------------------------------------------------------------------------------------
#you can see in x data one value is vary small and one value is vary large
#so use standardScaler
from sklearn.preprocessing import StandardScaler
x_sc = StandardScaler()
x_train = x_sc.fit_transform(x_train)
x_test = x_sc.fit_transform(x_test)


#----------------------------------------------------------------------------------------------------------
#this data set value is discrete set of values
#so i use Classification variant
from sklearn.linear_model import LogisticRegression


#----------------------------------------------------------------------------------------------------------
#make traing model
classiftre = LogisticRegression(random_state=0)
classiftre.fit(x_train,y_train)


#----------------------------------------------------------------------------------------------------------
#pridict value
y_pred = classiftre.predict(x_test)


#----------------------------------------------------------------------------------------------------------
#making confusion metrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

cm
#cm define matrix of y_test and y_pred ,which place your actual value and predicted value is rigth or wrong
#total 0th place in x_test is 63+5 but our predicted value 63 0th only and other are 1 in place of 0
#total 1th place in x_test is 8+24 but our predicted value 24 1th only and other are 0 in place of 1
"""
          0  1
cm=   0  63  5
      1  8  24
      
      0 with 0 is right ,63
      1 with 1 is right ,24
"""

#----------------------------------------------------------------------------------------------------------
#so 63+24 place is true in 100 place
#find our accuracy
print(((cm[0][0]+cm[1][1])/(cm[0][0]+cm[1][1]+cm[1][0]+cm[0][1]))*100)

#----------------------------------------------------------------------------------------------------------




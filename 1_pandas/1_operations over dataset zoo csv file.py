# -*- coding: utf-8 -*-

#Basic data analysis and merge – sort operations over dataset zoo.csv

#read dataset and  write dataset, from file------------------------------------------------------
import pandas as pd


#read csv file-----------------------------------------------------------------------------------
dataset = pd.read_csv('zoo.csv')


#type of dataset---------------------------------------------------------------------------------
type(dataset)


#data type  of all individual column-------------------------------------------------------------
dataset.dtypes


#dimension of dataset----------------------------------------------------------------------------
dataset.ndim


#firt five row as output-------------------------------------------------------------------------
dataset.head()

dataset.head(6)

#last five row-----------------------------------------------------------------------------------
dataset.tail()

dataset.tail(3)


#random row as output----------------------------------------------------------------------------
dataset.sample()


#3 random row as output--------------------------------------------------------------------------
dataset.sample(3)


#see particular column---------------------------------------------------------------------------
dataset.animal


#multiple column as output-----------------------------------------------------------------------
dataset[['animal','water_need']]


#slicing operation--------------------------------------------------------------------------------
dataset[['animal','water_need']][3:8]


#show dataset information------------------------------------------------------------------------
dataset.info()


#------------------------------------------------------------------------------------------------
dataset.describe()

#mean means all value's sum devide by number of value 
#uniq_id mean = 22253 / 22 = 1011.5
#standerd deviation(std) = https://www.youtube.com/watch?v=1E7NU-uWalY
#calculate = https://www.calculator.net/standard-deviation-calculator.html
#minimum value in datset = min
#25% = 1022-1001 = 21 --> (21*25)/100 = 5.25 ---> 1001+5.25 = 1006.25
#maximum value in dataset = max


#way to create dataFrame--------------------------------------------------------------------------
dataset1 = pd.DataFrame([['elephant','vegetables'],['tiger','meat'],['kangaroo','vegetables'],['zebra','vegetables'],['dog','meal']],columns=['animal','food'])
dataset1


#merge operation----------------------------------------------------------------------------------
dataset.merge(dataset1)

#in this merge operation only similar dataset is exist
#in this dataset 'lion' and 'dog' is not there


#outer join---------------------------------------------------------------------------------------
#outer join will return every row from one specified table
dataset.merge(dataset1,how='outer')

#in this dataset 'lion' and 'dog' is there


#left outer join----------------------------------------------------------------------------------
#leftTable.merge(rightTable,how='left')
dataset.merge(dataset1,how='left')

#in this dataset 'lion' is there but 'dog' is not there


#right outer join---------------------------------------------------------------------------------
#leftTable.merge(rightTable,how='right')
dataset.merge(dataset1,how='right')

#in this dataset 'dog' is there but 'lion' is not there


# same as a dataset.merge(dataset1)----------------------------------------------------------------
dataset.merge(dataset1,how='inner')


# value sorting in ascending order-----------------------------------------------------------------
dataset.sort_values('water_need')


# value sorting in descending order-----------------------------------------------------------------

dataset.sort_values('water_need',ascending=False)


#you can see our main dataset is not change----------------------------------------------------------
dataset


#you can use -->> inplace=True  than your all data set will be permanently change--------------------
dataset.sort_values('water_need',ascending=False,inplace=True)
dataset

#you also use for permanently store "dataset = dataset.sort_values('water_need',ascending=False,inplace=True)"
#you can use dataset.reset_index() for reset your index


#you want to filling NaN to some text-------------------------------------------------------------------
dataset.merge(dataset1,how='outer').fillna('Missing')


#--------------------------------------------------------------------------------------------------------
print(dataset[['animal','water_need']].max())
print(dataset[['animal','water_need']].min())
print(dataset[['animal','water_need']].mean())
print(dataset[['animal','water_need']].std())


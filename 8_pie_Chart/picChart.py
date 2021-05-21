# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:31:00 2021

@author: Aksh
"""


#--------------------------------------------------------------------------------------------
# pie chart
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------------------------
a = [1,2,3,4,5]
b = ['A','B','C','D','E']
plt.pie(a,labels=b)
plt.savefig("pieChart.png")

#--------------------------------------------------------------------------------------------
#read csv
import pandas as pd
myCsv = pd.read_csv("Social_Network_Ads.csv")
myCsv.head()

#--------------------------------------------------------------------------------------------
#find male in myCsv
myCsv['Gender'] == 'Male'
male  = myCsv.loc[myCsv['Gender'] == 'Male'].count()[1]

#--------------------------------------------------------------------------------------------
#find female in myCsv
female  = myCsv.loc[myCsv['Gender'] == 'Female'].count()[1]

#--------------------------------------------------------------------------------------------
#make pie chart
lable = ['male Data','female Data']
color = ['#a7d129','#ff0000']
explo = (0.1,0)
#use autopct for show percentage
plt.pie([male,female],labels=lable,colors=color,autopct='%.2f%%',explode=explo)
plt.savefig("CountMF.png")


#--------------------------------------------------------------------------------------------
#find male salary using loc
low = myCsv.loc[(myCsv['Gender'] == 'Male') & (myCsv['EstimatedSalary']<=20000)].count()[1]

medium = myCsv.loc[(myCsv['Gender'] == 'Male') & (myCsv['EstimatedSalary'] > 20000) & (myCsv['EstimatedSalary'] <= 70000)].count()[1]

high = myCsv.loc[(myCsv['Gender'] == 'Male') & (myCsv['EstimatedSalary'] > 70000)].count()[1]

x = [low,medium,high]

y = ['low salary','Medium salary','High salary']

color = ['#ffd700','#a7d129','#d72323']
plt.pie(x,labels=y,colors=color,autopct='%.2f%%')
plt.savefig("LMHLoc.png")

#--------------------------------------------------------------------------------------------
#find Female salary using iloc
lowF = myCsv.iloc[(myCsv['Gender'] == 'Female').values & (myCsv['EstimatedSalary']<=20000).values,[3]].count()

mediumF = myCsv.iloc[(myCsv['Gender'] == 'Female').values & (myCsv['EstimatedSalary'] > 20000).values & 
                    (myCsv['EstimatedSalary'] <= 70000).values,[3]].count()

highF = myCsv.iloc[(myCsv['Gender'] == 'Female').values & (myCsv['EstimatedSalary'] > 70000).values,[3]].count()

x = [lowF.EstimatedSalary,mediumF.EstimatedSalary,highF.EstimatedSalary]

y = ['low salary','Medium salary','High salary']

color = ['#ffd700','#a7d129','#d72323']
explo = (0.4,0.1,0.1)
plt.title("Female Salary",y=-0.11,fontdict={'fontname':'Comic Sans MS','fontsize':15})
plt.pie(x,labels=y,colors=color,autopct='%.2f%%',explode=explo)
plt.savefig("LMHuseIloc.png")









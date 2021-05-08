# -*- coding: utf-8 -*-
"""
Created on Sun May  2 10:57:10 2021

@author: Aksh
"""


#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8]
y = [0,2,4,6,8,6,4,2,0]

#demo example-1 ------------------------------------------------------------------------------------------------
plt.plot(x,y)
plt.title("Demo Example")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig("firstplot.png")

#demo example-2 ------------------------------------------------------------------------------------------------
plt.plot(x,y)
plt.title("Demo Example",fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.xlabel('x-axis',fontdict={'fontname':'Times New Roman','fontsize':20})
plt.ylabel('y-axis')
plt.savefig("secondplot.png")


#demo example-3-------------------------------------------------------------------------------------------------
plt.plot(x,y,label='X with Y graph',color='red',linewidth=2,marker='o',markersize=10,markeredgecolor='blue')

#you want to use more marker follow this link https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
plt.legend() #you want to add label then you must have add legend

#add ticks for show number on x and y axis
plt.xticks([0,2,4,6,8])
plt.yticks([0,1,2.5,3,4,5.5,6,7,8.5])

plt.title("Demo Example")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig("thirdplot.png")
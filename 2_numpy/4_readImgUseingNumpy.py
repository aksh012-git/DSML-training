# -*- coding: utf-8 -*-
"""
Created on Sat May  1 00:04:11 2021

@author: Aksh
"""


import numpy as np

#for import img
from skimage import io

god_img = io.imread('god.jpg')
print(god_img)
print(god_img.ndim)
print(god_img.shape)
#(640,640,3) ---> 3 means it's a color img R G B, and dimension is 640 x 640

#pixel value of every img is 0 to 255
#min and max pixel value
print(god_img.min(),god_img.max())


#how to generate rendom img
import matplotlib.pyplot as plt
rand_img = np.random.random([500,500])

#rand_img dimension is 500 x 500
plt.imshow(rand_img)
plt.savefig('myRandImg.jpg')

#god_img dimension is 640 x 640
plt.imshow(god_img)
plt.savefig('godimg.jpg')

dark_img = god_img * 0.5
plt.imshow(dark_img)
plt.savefig('darkImg.jpg')


#make blue img [R,G,B] = [0.,0.,1.]
blue_img = god_img * [0.,0.,1.]
plt.imshow(blue_img)
plt.savefig('blueimg.jpg')


#you can change some portion color of your img
#in my case i change 50th row to 300row and 50th coulmn to 300th column change color and make as green
#god_img[row,column,color]
god_img[50:300,30:300,:] = [0,255,0]
plt.imshow(god_img)
plt.savefig('greenportion.jpg')

#case 2 multi color
god_img[50:300,0:300,:] = [255,0,0] #red
god_img[300:400,300:400,:] = [0,255,0] #green
god_img[400:600,0:300,:] = [0,0,255] #blue
god_img[50:300,400:600,:] = [128,0,128] #purple
god_img[400:600,400:600,:] = [255,255,255] #white
plt.imshow(god_img)
plt.savefig('multicolor.jpg')






# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 14:09:07 2021

@author: Aksh
"""


from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')


#find main container
find_main = soup.find('main',class_='content')

#make and write csv file 
import csv
csv_file = open('2_mycsv.csv','w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Headline','summery','vidio_link'])


for x in find_main.find_all('article'):
    
    try:
        
        #find header of vidio content
        header_text = x.header.h2.text
        
        #print(header_text+ "\n")
        
        #find vidio description
        description_text = x.find('div',class_='entry-content').p.text
        
        #print(description_text+ "\n")
        
        #find link of youtube video
        link = x.find('div',class_='entry-content').find('iframe')['src']
        video_id = link.split('/')[4]
        vidio_idFine = "https://www.youtube.com/watch?v=" + video_id.split('?')[0] 
        
        #print(vidio_idFine + "\n")
        w = " "
    except:
        vidio_idFine="not found"
        
        #print("somthing missing \n")
    #print("----------")
    
    #write data in CSV file
    csv_writer.writerow([header_text,description_text,vidio_idFine])    
    
csv_file.close()


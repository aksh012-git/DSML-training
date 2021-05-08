# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:50:31 2021

@author: DELL
"""

# Importance of Programming in science and engineering 
# field to give problem solution

# We are in need of dataset to work with

# Web Scraping

# Scrapy, Selenium, BeautifulSoup
# Assignment -1  - Identify which one is better: 
# Scrapy, Selenium, BeautifulSoup?

from bs4 import BeautifulSoup
import requests

## We want to read content from sample.html.
## It is having subject1 link  and it's description
## Same way for subject 2

# Let's open Website URL OR Web-Page path in read mode
with open('1_sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# lxml - is a parser

#f = open('sample.html','r')
#f

print(soup)

# If we found output, which is not formatted properlly, 
# then for the look and feel with proper indentation
print(soup.prettify())

# To display only title element
match = soup.title
print(match)

# To display only title - without tag
match = soup.title.text
print(match)

# To find any specific tag (div) in body - 
match = soup.div # this returns only first div tag element
print(match)

match = soup.div.text # this returns only first div tag element
print(match)
match = soup.text
print(match)
# Another way to do same is:
match = soup.find('div')
print(match)

match = soup.find('div').text
print(match)

# This 2nd approach with find method gives us a more attributes 
# to add for micro level analysis
# As class is a keyword, we require to add _ sign class_

match = soup.find('div', class_='footer')
print(match)

match = soup.find('div', class_='footer').text
print(match)

# Now, right click on web page content and inspect element
# And let's try to print first div content
sub = soup.find('div', class_='sub')
print(sub)

# now, to go more in deep, find h2 in sub, then a and display its text

match = soup.div.h2.a.text
print(match)

heading = sub.h2.a.text
print(heading)

summary = sub.p.text
print(summary)

# to find all the tags that match the argument, we should go with find_all
sub = soup.find_all('div', class_='sub')
print(sub)

for sub in soup.find_all('div', class_='sub'):
    heading = sub.h2.a.text
    print(heading)
    
    summary = sub.p.text
    print(summary)
    







































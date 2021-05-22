# -*- coding: utf-8 -*-
"""
Created on Sat May 22 09:10:27 2021

@author: Aksh
"""


"""
1) what is NLP?
- Natural Language Processing, or NLP for short, is broadly defined as the automatic 
  manipulation of natural language, like speech and text, by software.

2)Application of NLP
-speech recognition like google Assistant or siri
-sentimental analysis like you can analyze twitter tweet
-machine translation like google translate
-chat bots like AI chat box

3)main NLP library:-
- NLTK-natural language Tollkit
- SpaCy
- Stanford NLP
- OpenNLP

4)install library
- open anaconda prompt and 'pip install NLTK'

"""

#--------------------------------------------------------------------------------------------------------------------
#step 1 read file
#our file is .tsv so use delimiter for tsv file
import pandas as pd
#quoting=3 indicate NONE, use for you want to avoid quoting in your dataset
myfile = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t',quoting=3)

#--------------------------------------------------------------------------------------------------------------------
#step 2 Data pre-processing or Data clening
#use library 're' stands for "regular expression"
import re

# re.sub(pattern, repl ,string)
#pattern - what you keep in this data
#replace(repl) - anything other than pattern,then replace with what 
review1 = re.sub('[^a-zA-Z]',' ',myfile['Review'][0])
review1 = review1.lower()
review1 = review1.split()

"""
wow loved this place 
wow love this place 
wow loving this place 
wow loves this place 

-All meaning are same
"""

#--------------------------------------------------------------------------------------------------------------------
#first import NLTK library
import nltk

#stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

"""
removing stop words in any language
like remove stop words ---->>> i am enjoing food -->> enjoy food
"""
w = []
#apply stop words for removing stop word,you can apply stop words in any language 
for word in review1:
    if not word in set(stopwords.words('english')):
        w.append(word)
    
#apply PorterStemmer for make your english word in original english word
#you can not write "from nltk.stem.porter import PorterStemmer"
from nltk.stem import PorterStemmer
ps = PorterStemmer()

w1 = []
for word in w:
    w1.append(ps.stem(word))

review1 = w1   

#----------------------- same step in short --------------------------------------------------------------------------
#first import NLTK library
import nltk

#stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

#you can write also "from nltk.stem import PorterStemmer"
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

#you can apply same thing in one line
review1 = [ps.stem(word) for word in review1 if not word in set(stopwords.words('english'))]

#join list 
review1 = ' '.join(review1)

#----------------------------All in one------------------------------------------------------------------------------
#all review clean in one
new_data_set = []
for i in range(0,1000):
    review = re.sub('[^a-zA-Z]',' ',myfile['Review'][i])
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    new_data_set.append(review)































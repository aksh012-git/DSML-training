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

#-------------------------------------------------------------------------------------------------------------------
#Use countvectorizer for convert your catogarial data to numerical data
#countvectorizer - https://www.geeksforgeeks.org/using-countvectorizer-to-extracting-features-from-text/
from sklearn.feature_extraction.text import CountVectorizer

#in your dataset many uniqe categorical value is there 
#you apply countvectorizer for all value than matrix made vary large
#so you use few value in entire dataset then use "max_features=how many value you choose randomly"
#most frequently used words choose by system randomly
cv  = CountVectorizer(max_features=1500)

#convert data into "sparse matrix"
x = cv.fit_transform(new_data_set).toarray()
#then x become our input data

#y is our output column
y = myfile.iloc[:,1].values

#-------------------------------------------------------------------------------------------------------------------
#split data into training and testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state = 0)


#-------------------------------------------------------------------------------------------------------------------
#use naive bayes classification variants 
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
#tarin your model
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

#-------------------------------------------------------------------------------------------------------------------
#see your x data then 0th row only 3 column are 1 and othre 1497 column having 0 value
#because "wow love place" is in 0th row then 3 words only so 3 non-zero row in x othre having zero

#to hold only non zero values - we can help of variation of "orginal sparse matrix"
#other veriant is "CSR matrix - compressed sparse row matrix" and etc.

#example - CSR matrix
import numpy as np
arr = np.array([[0,0,0],
                [8,0,0],
                [0,5,4],
                [0,0,0],
                [0,0,7]])

#for compresse your matrix
from scipy.sparse import csr_matrix
demo = csr_matrix(arr)

print(demo.data) #print your data
print(demo.indices) #print indices or column of your data (this is a column related information)
print(demo.indptr) # if you having n rows then getting n+1 values 

"""
[8 5 4 7] - data
[0 1 2 2] - indices / column
[0 0 1 3 3 4] - indptr

indptr = 6 value 
then our row is 6 - 1 = 5 row in our matrix

-in indptr 
0 - 0 = 0 so 0th row is empty means no any non zero element in our 0th row
1 - 0 = 1 so 1st row having one element
3 - 1 = 2 so 2nd row having two element
3 - 3 = 0 so 3rd row having zero element
4 - 3 = 1 so 4th row having one element

set element->>
- 8 is 0th indices and 1st row
- 5 is 1st indices and 2nd row
- 4 is 2nd indices and 2nd row
- 7 is 2nd indices and 4th row


in our data arr is 5 x 3 = 15 element
and our csr matrix 4 data + 4 indices + 6 indptr = 14 element

suppose our matrix is 100 x 100 = 1000 element and 50 non zero element
then csr is 50 value + 50 indices + 101 indptr(row+1) = 201 element only 
this is vary useful for compresse your matrix and neglect zero elements
"""

#-------------------------------------------------------------------------------------------------------------------













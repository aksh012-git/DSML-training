# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:22:40 2021

@author: Aksh
"""


"""
How to connect our ML model to web application

you can connect with django and flask base wab application

step 1 - open anaconda prompt
step 2 - conda install flask 

"""

#import flask
from flask import Flask,render_template,url_for,request


#in one project many python file available then you want to execute main python file then this name is __main__
#so i put name as __name__
#and put in flask
app = Flask(__name__)

#define default route of web app and difine which file you want to execute this route
@app.route('/')
def index():
    return render_template('index.html')
#render_template is go to the tamplates folder and search 'index.html' file
    

#you want to run your project then go to anaconda prompt
#go to yor folder path
#and write "python first.py"


  
import pandas as pd
#use for count vectorizer
from sklearn.feature_extraction.text import CountVectorizer
#for read our pkl file
from sklearn.externals import joblib

@app.route('/predict', methods=['POST'])
def predict():
    df = pd.read_csv("names_dataset.csv")
    
    #split input and output column
    df_x = df.name
    df_y = df.sex
    
    corpus = df_x
    #make Count Vectorizer reference variable 
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)
    #rb means read binary string 
    clf = joblib.load(open("models/naivebayesgendermodel.pkl","rb"))
    
    if request.method == 'POST':
        pname = request.form['pname']
        
        #convert data into 1D array and our data is categorical 
        data = [pname]
        #convert categorical data to numerical data using count vectorizer
        vect = cv.transform(data).toarray()
        #and our model is store in clf variable then predict our vect so passing our vect to our model
        pred = clf.predict(vect)
        #render_template is search in our template folder and find results.html
    return render_template('results.html',prediction=pred,name = pname.upper())
    
    
if __name__ == '__main__':
    app.run(debug=True)   
    
    
    
    
    
    
"""
our pkl file model is already exist then why we need CountVectorizer-->
bcz i write in input on html then this data is categorical format so i replace to a numerical data then i use CountVectorizer
"""   
    
    
    
    
    
    
    
    
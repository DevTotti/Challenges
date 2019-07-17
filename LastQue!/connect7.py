import mechanicalsoup
import re
import json
import csv, sys
import requests
from statistics import mean
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd
import scipy
import scipy.stats as st
from scipy.spatial.distance import cdist
from scipy.interpolate import *
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split


style.use('fivethirtyeight')


s=requests.Session()
dictt = {}

#load the facebook cookie json data
with open('facebook_cookie.json') as fb:
    load = json.load(fb)

def get_friends_data():
    dictt = {}
    friends_data = []
    for cookie in load:
        s.cookies.set(cookie['name'], cookie['value'])

    url = 'https://web.facebook.com/search/100002743322368/friends?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s)
    browser.open(url)
    friends = str(browser.get_current_page())
    gender= ''
    friends = friends.split('class="_32mo"')
    for i in friends:
        match_name = re.compile(r'EntRegularPersonalUser"><span>([a-zA-Z0-9\-\s]+)')
        names = match_name.search(i)
        if names == None:
            continue
        else:
            dictt['Name'] = names.group(1)
            name = names.group(1)
            name = name.lower()
            name = name.split()
            name = ".".join(name)
            browser.open('https://web.facebook.com/' + name +'/about?section=contact-info&_rdc=1&_rdr')
            page = str(browser.get_current_page())
            page = page.split('class="_50f4 _5kx5"')
            for i in page:
                matchgender = re.compile(r'<div><span class="_2iem">([a-zA-Z]+)')
                match_gender = matchgender.search(i)
                if match_gender == None:
                    continue
                else:
                    dictt['Gender'] = match_gender.group(1)


            friends_data.append(dictt.copy())
    fd = open('friends_data.json','wb')
    json.dump(friends_data,fd)


def predict_gender():
    #read and open data file using the pandas built-in read method
    df = pd.read_csv('friends_data.csv')
    #drop the name column as it won't help get the real values and accuracy
    df.drop(['Name'],1, inplace=True)

    #assign other columns except the Gender to the X axis
    X = np.array(df.drop(['Gender'], 1))

    #assign the Gender column to the y axis
    y = np.array(df['Gender'])

    #train and test
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y, test_size = 0.2)

    #get the knearest neighbors classifier working
    clf = neighbors.KNeighborsClassifier()
    #fit it into the x and y train
    clf.fit(X_train, y_train)

    #using the clf.score, get the accuracy of the data
    accuracy = clf.score(X_test, y_test)
    print("The accuracy of the Data is: ",accuracy)

    #we predict with an example
    example_measures = np.array([12,231])#12 for male friends and 231 for female friends
    #NOTE: The accuracy and prediction accuracy of this algorithm depends solely on the imported dataset
    #Reshape the example to work fine
    example_measures = example_measures.reshape(-1, len(example_measures))

    #Make our predictions using the clf.predict method
    prediction = clf.predict(example_measures)
    print ("Prediction of Gender of user is : "+prediction)


get_friends_data()
predict_gender()

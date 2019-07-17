"""
Name: Osuntolu  Paul
email: neptunecody@gmail.com

Intermediate test question 5 & 6
"""

import mechanicalsoup
import re
import json
import requests
from statistics import mean
import scipy
import scipy.stats as st
from scipy.spatial.distance import cdist
from scipy.interpolate import *
import numpy as np

s=requests.Session()

#load the facebook cookie json data
with open('facebook_cookie.json') as fb:
    load = json.load(fb)

#start by taking the female friend
#define a function to for the female friends
def get_female_friends():
    dictt = {}
    female_friends = []
    for cookie in load:
        s.cookies.set(cookie['name'], cookie['value'])
    url = 'https://web.facebook.com/search/100002743322368/friends/intersect/females/intersect?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s)
    browser.open(url)
    f_page = str(browser.get_current_page())
    f_page = f_page.split('class="_ajw"')
    for i in f_page:
        match_name = re.compile(r'EntRegularPersonalUser"><span>([a-zA-Z0-9\-\s]+)')
        names = match_name.search(i)
        details = re.compile(r'show="1">([a-zA-Z0-9.\-\s]+)')
        details = details.search(i)
        in_fo = re.compile(r'class="_52eh">([a-zA-Z0-9.\-\s]+)')
        info = in_fo.search(i)
        if names == None :
            continue
        else:
            dictt["name"] = names.group(1)
            dictt["details"] = details.group(1)
            #dictt["info"] = info.group(1)

            female_friends.append(dictt.copy())

    ff = open('female_friends.json','wb')
    json.dump(female_friends, ff)

    friendsfemale = len(dictt["name"])
    return friendsfemale

#get the data for the pages liked by user
#define a function for pages liked
def get_pages_liked():
    dictt = {}
    pages_likes = []
    for cookie in load:
        s.cookies.set(cookie['name'], cookie['value'])
    url = 'https://web.facebook.com/search/100002743322368/pages-liked?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s)
    browser.open(url)
    l_page = str(browser.get_current_page())
    l_page = l_page.split('class="_ajw"')
    for i in l_page:
        match_name = re.compile(r'EntConcreteOwnedPage"><span>([a-zA-Z0-9\-\s]+)')
        p_names = match_name.search(i)
        likes = re.compile(r'class="_glm">([a-zA-Z0-9.\-\s]+)')
        likes = likes.search(i)
        detail = re.compile(r'class="_52eh"><span>([a-zA-Z0-9.\-\s]+)')
        detail = detail.search(i)

        if p_names  == None:
            continue
        else:
            dictt["name"] = p_names.group(1)
            #dictt["likes"] = likes.group(1)
            #dictt["detail"] = detail.group(1)
            pages_likes.append(dictt.copy())

    pl = open('pages_likes.json','wb')
    json.dump(pages_likes, pl)
    #pages_liked = len(dictt['name'])

    return pl

def get_mutual_friends():
    dictt = {}
    mutual_frn = []
    for cookie in load:
        s.cookies.set(cookie['name'], cookie['value'])
    url = 'https://web.facebook.com/search/100002743322368/friends/intersect/females/intersect?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s)
    browser.open(url)
    mutual = str(browser.get_current_page())
    mutual = mutual.split('class="_ajw"')
    for i in mutual:
        match_name = re.compile(r'EntRegularPersonalUser"><span>([a-zA-Z0-9\-\s]+)')
        m_names = match_name.search(i)
        m_details = re.compile(r'show="1">([a-zA-Z0-9.\-\s]+)')
        m_details = m_details.search(i)
        m_in_fo = re.compile(r'class="_52eh">([a-zA-Z0-9.\-\s]+)')
        m_info = m_in_fo.search(i)

        if m_names == None :
            continue
        else:
            dictt["name"] = m_names.group(1)
            #dictt["info"] = m_info.group(1)
            dictt["details"] = m_details.group(1)
            mutual_frn.append(dictt.copy())

    mf = open('mutual_friends.json','wb')
    json.dump(mutual_frn, mf)

    mutual_friends = len(dictt["name"])
    return mutual_friends



mutual_friends=get_mutual_friends()
pl=get_pages_liked()
friendsfemale=get_female_friends

def confidence_interval(loads, confidence = 0.78):
    #loads = (get_pages_liked, get_female_friends, get_mutual_friends)
    a = 1.0*(np.array(loads))
    n = len(a)
    loc, scale = np.mean(a), st.sem(a)

    chosen_range = (45, 60)
    confidence_interval(chosen_range)
    st.t.interval(0.78, len(a)-1,loc=np.mean,scale=st.sem(a))

loads = (friendsfemale, pl, mutual_friends)
confidence_interval(loads, confidence=0.78)

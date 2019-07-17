"""
Name: Osuntolu  Paul
email: neptunecody@gmail.com

Intermediate test question 1
"""

#The url for the friends post is broken
import mechanicalsoup
import re
import json
import requests

friends_post = []
dictt = {}
s=requests.Session()

#open and load the facebook cookie json file
with open('facebook_cookie.json') as c:
    load = json.load(c)

#define a function to get friends posts
#the url is not working well
def get_friends_post():
    for cookie in load:
        s.cookies.set(cookie['name'], cookie['value'])

    #url for facebook page
    url = 'https://www.facebook.com/search/str/friends+posts/keywords_search?fb_dtsg_ag=Ady4zI0V_8B-bvHeCxqmAtbDltrCvfdyZ9iujg466IUwww%3AAdyqGU3y01Sz342h9AdhmI6ELQGOax-TEpFBaB6wJiGN9g&filters_rp_author=%7B%22name%22%3A%22author_friends_groups%22%2C%22args%22%3A%22%22%7D'

    #initialize the mechanicalsoup StatefulBrowser
    browser = mechanicalsoup.StatefulBrowser(session=s)

    #open url with the mechanicalsoup browser
    browser.open(url)

    #define posts in the page and get it in for of str
    posts = str(browser.get_current_page())

    #get the string converted posts data
    posts = posts.split('class="_ajw"')

    #iterate through the posts
    for i in posts:
        #using regular expression, match,compile and search for elements
        match_name = re.compile(r'show="1">([a-zA-Z0-9\-\s]+)')
        name = match_name.search(i)
        match_time = re.compile(r'timestampContent">([a-zA-Z0-9\-\s]+)')
        time = match_time.search(i)
        match_post = re.compile(r'<span.*? data-ft.*?>([a-zA-Z0-9.\s]+)')
        fr_post = match_post.search(i)


        if name == None:
            #print ("No match")
            continue
        else:
            dictt["name"] = name.group(1)
            dictt["Since When"] = time.group(1)
            dictt["Post"] = fr_post.group(1)
            friends_post.append(dictt.copy())

    #create a json file to save the extracted data from and dump data to it
    f = open('Friends_post.json','wb')
    json.dump(friends_post, f)

    
    return f

get_friends_post()

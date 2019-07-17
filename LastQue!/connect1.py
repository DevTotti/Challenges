

import mechanicalsoup
import re
import json
import requests

friends_post = []
dictt = {}
s=requests.Session()

with open('facebook_cookie.json') as c:
    load = json.load(c)
def get_friends_post():
    for cookie in load:
        s.cookies.set(cookie['name'], cookie['value'])

    url = 'https://www.facebook.com/search/100002743322368/friends/intersect/males/intersect?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s)
    browser.open(url)

    posts = str(browser.get_current_page())
    posts = posts.split('id="u_2f_m"')
    for i in posts:
        match_name = re.compile(r'show="1">([a-zA-Z0-9\-\s]+)')
        name = match_name.search(i)
        match_time = re.compile(r'timestampContent">([a-zA-Z0-9.\-\s]+)')
        time = match_time.search(i)
        match_post = re.compile(r'<span.*? data-ft.*?>([a-zA-Z0-9.\s]+)')
        fr_post = match_post.search(i)

        if name == None:
            print ("No match")
            continue
        else:
            dictt["name"] = name.group(1)
            dictt["Since When"] = time.group(1)
            dictt["Post"] = fr_post.group(1)
            friends_post.append(dictt.copy())

    f = open('Friends_post.json','wb')
    json.dump(friends_post, f)

get_friends_post()

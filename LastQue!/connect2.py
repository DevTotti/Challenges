

import mechanicalsoup
import re
import json
import requests

friends_group = []
dictt = {}
s=requests.Session()

with open('facebook_cookie.json') as c:
    load = json.load(c)
def get_friends_group():
    for cookie in load:
        s.cookies.set(cookie['name'], cookie['value'])

    url = 'https://www.facebook.com/search/100002743322368/friends/groups?_rdc=1&_rdr'
    browser = mechanicalsoup.StatefulBrowser(session=s)
    browser.open(url)

    group_page = str(browser.get_current_page())
    group = group_page.split('class="_ajw"')
    for i in group:
        match_name = re.compile(r'ref=br.rs">([a-zA-Z0-9\-\s]+)</a>')
        name = match_name.search(i)
        match_members = re.compile(r'(<div class="_pac")(.*?)([a-zA-Z0-9\s]+)<')
        members = match_members.search(i)
        match_friends = re.compile(r'show="1">([a-zA-Z0-9.\-\s]+)')
        group_friends = match_friends.search(i)

        if name == None:
            continue

        else:
            dictt["Group"] = name.group(1)
            dictt["Members"] = members.group(3)
            #dictt["Friends_in_group"] = group_friends.group(2)
            friends_group.append(dictt.copy())

    f = open('Friends_groups.json','wb')
    json.dump(friends_group, f)

get_friends_group()

"""
Name: Osuntolu  Paul
email: neptunecody@gmail.com

Intermediate test question 4
"""

#import important libraries like the psycopg2, json, time
import psycopg2
import json
import time

#open and load json files for facebook cookie
with open('facebook_cookie.json') as fb:
    login = json.load(fb)

#define a function for registering the facebook cookie into database
def insert_cookie_into():
    #getting user and databse details from user
    db = raw_input("Enter your database name: ")
    us = raw_input("Enter your username: ")
    pw = raw_input("Enter your password: ")
    #hs = raw_input("Enter database localhost here, use 'localhost' as default: ")
    #pt = int(input("Enter database port, use '5432' as default: "))
    print "Done!"

    #sleep the system for 2 seconds and continue
    time.sleep(2)
    #connect to database using the credentials defined above
    connection = psycopg2.connect(database = db, user = us, password = pw, host = 'localhost', port = '5432')
    #activate cursor
    cur = connection.cursor()

    #use cursor to execute table creating command
    cur.execute('''CREATE TABLE FacebookCookie
                (
                id          serial PRIMARY KEY,
                domain      text not null,
                name        text not null,
                value       text not null,
                path        text not null,
                httpOnly    text not null,
                secure      text not null,
                expiry      text not null);''')
    time.sleep(2)
    #successful
    print "Tables successfully created"
    connection.commit()

    #initialize the database insertion commands
    database = """INSERT INTO Cookies(domain,name,value,path,httpOnly,secure,expiry)VALUES(%s,%s,%s,%s,%s,%s,%s);"""

    #loop through data from json file
    for keys in login:
        #execute command
        cur.execute(database,(keys['domain'],keys['name'],keys['value'],keys['path'],keys['httpOnly'],keys['secure'],keys['expiry']))
        connection.commit()
        #close the database connection
    connection.close()


with open('facebook_cookie.json') as fb:
    frgroup = json.load(fb)
def grops_of_friends():
        db = raw_input("Enter your database name: ")
        us = raw_input("Enter your username: ")
        pw = raw_input("Enter your password: ")
        #hs = raw_input("Enter database localhost here, use 'localhost' as default: ")
        #pt = int(input("Enter database port, use '5432' as default: "))
        print "Done!"

        time.sleep(2)
        connection = psycopg2.connect(database = db, user = us, password = pw, host = 'localhost', port = '5432')
        cur = connection.cursor()

        cur.execute('''CREATE TABLE FriendsGroup
                    (
                    id          serial PRIMARY KEY,
                    group      text not null,
                    members      text not null);''')
        time.sleep(2)
        print "Tables successfully created"
        connection.commit()

        database = """INSERT INTO FriendsGroup(group,members)VALUES(%s,%s);"""

        for keys in frgroup:
            cur.execute(database,(keys["Group"],keys["Members"]))
            connection.commit()
        connection.close()

#call functions
grops_of_friends()
insert_cookie_into()

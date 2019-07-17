"""
NAME:   OSUNTOLU PAUL ADEDIRAN
EMAIL:  neptunecody@gmail.com
PHONE:  09025111684

Question B :Store data scrapped from webpage in database using postgresql
"""

#import regular expression, urllib library and psycopg2
import re
import urllib, urllib2
import psycopg2


#open webpage file using urllib.urlopen and read using the .read()
files = urllib.urlopen("python_class_test.html")
file = files.read()

#define a function for the regular expression matched
def expression():

    #create a pattern to match the color
    pattern = re.compile(r'<td>([A-Z]+, \w.*?)</td>')

    #find all matched pattern
    matches = re.findall(pattern, file)

    #iterate through the patterns matched
    for match in matches:

        #splt items in matched
        items = match.split()

        #record items matched in a dictionary
        d = {x: items.count(x) for x in items}
        print d

#Prompt user for credentials for Accessing Database
db = raw_input("Enter your database name: ")
us = raw_input("Enter your databse username: ")
pw = raw_input("Enter your database password: ")
hs = raw_input("Enter your database localhost, use 'localhost' as default: ")
pt = int(input("Enter the databse port,use '5432' as default: "))
print "Accessing database, please wait"
conn = psycopg2.connect(database = db, user = us, password = pw, host = hs, port = pt)
cur = conn.cursor()
print "Done!"

#Defines a function to create Table
def create_data():

    #Create table within the range of files reading using a for loop
    for i in range(len(file)):

        #create tables
        cur.execute("""CREATE TABLE         COLORCODES
                       (COLORS               TEXT NOT NULL,
                       FREQUENCIES          INT NOT NULL);""".format(file[i][0:8].upper()))

        #Prints a Success message
        print ("Table COLORCODES created successfully!")

#Defines a function for inserting values to tables created into the database
def InsertInto():

    #insert within the range of files reading using for loop
    for i in range(len(file)):

        #read lines of each file to find related pattern
        for line in file.readlines():

            #find matches in file read
            matches = re.findall(pattern, line)

            #if match found then insert into DB tables
            if tally:
                database = "INSERT INTO COLORCODES(COLORS, FREQUENCIES) VALUES (%s, %s)".format(file[i][0:8].upper())
                for item in tally:

                    #index of tables created
                    colors = item[0]
                    frequency = item[1]

                    #execute the insertion command then commit
                cur.execute(database,(colors, frequency))
                conn.commit

#call defined functions
expression()
create_data()
InsertInto()

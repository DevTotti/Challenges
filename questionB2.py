"""
NAME:   OSUNTOLU PAUL ADEDIRAN
EMAIL:  neptunecody@gmail.com
PHONE:  09025111684

Question B :Store data scrapped from webpage as a dictionary, using colors as key
and frequency as values
"""

#import regular expression, urllib library
import re
import urllib, urllib2


#open webpage file using urllib.urlopen and read using the .read()
file = urllib.urlopen("python_class_test.html")
file = file.read()

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

"""
        #record items matched in a dictionary
        diction = {x: items.count(x) for x in items}
        print diction

        count = 0.0
        sum = 0.0
        for key in diction:
            count += 1
            sum += diction[key]
        print ("The mean is: ",sum/count)
"""
expression()

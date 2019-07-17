#import regular expression, urllib library, numpy
import re
import urllib, urllib2
import numpy as np

#open webpage file using urllib.urlopen and read using the .read()
file = urllib.urlopen("python_class_test.html")
file = file.read()

#define a function for the regular expression matched
def expression():

    #create a pattern to match the color
    pattern = re.compile(r'<td>([A-Z]+, \w.+?)</td>')

    #find all matched pattern
    matches = re.findall(pattern, file)

    #iterate through the patterns matched
    for match in matches:
        print match

        #split the items in the matched list
        items = match.split()
        freq = []
        for stuffs in items:
            freq.append(items.count(stuffs))
        #print(str(items)+ "\n")
        print (str(zip(items,freq)))

        #to calculate the mean, use the numpy,mean function
        a = np.mean(freq)
        print a

#call function
expression()
#mathFunction()

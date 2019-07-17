"""
Name: Osuntolu  Paul
email: neptunecody@gmail.com

Intermediate test question 3
"""


#import important libraries
import selenium
import json
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import requests
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException

s = requests.Session()

#make user input their details for fcebook
email = raw_input("Enter your facebook login username/email: ")
password = raw_input("Enter your facebook password: ")

#get the chrome driver from executable path
def get_driver():
    #load chrome webdriver
    driver = webdriver.Chrome(executable_path = '/home/gitvee/workspace/extensions/chromedriver_linux64/chromedriver')
    #wait 3 seconds for the driver to initialize
    driver.wait = WebDriverWait(driver, 3)
    #return driver properties
    return driver

#get the url and cookie from chrome
def get_url_cookie(driver):
    driver.get('https://facebook.com')#get the url with chrome

    #find the login credentials by element name
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('pass').send_keys(password)
    #wait for 3 seconds
    time.sleep(3)
    driver.find_element_by_id('loginbutton').click()#then click on the login button
    #get cookies of successful user login
    cookies_list = driver.get_cookies()
    #open the .json file
    javascript = open('facebook_cookie.json', 'w')
    #dump the cookies in the json file
    json.dump(cookies_list, javascript)

def use_data():
    with open('facebook_cookie.json') as c:
        load = json.load(c)
    cookies_dict = []
    for cookie in load:
        cookies_dict.append[cookie['name']], [cookie['value']]
    session_id = cookies_dict.get('session')
    print(session_id)

#call the functions defined
driver = get_driver()
get_url_cookie(driver)

#quit the driver and the browser
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
browser.get('https://www.facebook.com/')

user = input("Enter FB user mail")
password = input("Enter password")

elem = browser.find_element_by_id("email")
elem.send_keys(user)

elem = browser.find_element_by_id("pass")
elem.send_keys(password + Keys.ENTER)

print("Logged into FB")

browser.close()

import time
from selenium import webdriver
import bs4
import requests
import getpass
import sys
from backend import *
import pandas as pd

data = pd.read_csv("requirements.csv")

try:
    browser=webdriver.Chrome(r"C:\Users\djsam\Desktop\Files\Selenium_Drivers\chromedriver")
except:
    browser=webdriver.Firefox()

browser.maximize_window()
browser.implicitly_wait(20)
browser.get("https://www.instagram.com/")
time.sleep(1)

userID = data["username"][0]
try:
    userPasscode = GET_old_passcode()
except:
    userPasscode = data["password"][0]
    f = open("old_code.txt", "w")
    f.seek(0) 
    f.write(userPasscode)
    f.close()

login_username_Field=browser.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
login_username_Field.send_keys(userID)

login_passcode_Field=browser.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")
login_passcode_Field.send_keys(userPasscode)

login_passcode_Field.submit()

time.sleep(10)
saveLogin = browser.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button")
if saveLogin:
    saveLogin.click()
notifNOTNOW=browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
notifNOTNOW.click()

browser.get("https://www.instagram.com/accounts/password/change/")

oldPasscodeEntry = browser.find_element_by_css_selector("#cppOldPassword")
oldPasscodeEntry.send_keys(GET_old_passcode())

APPEND_password(GET_old_passcode())

newPasscodeEntry = browser.find_element_by_css_selector("#cppNewPassword")
newPasscodeEntry.send_keys(generate_passcode(10))

confirmPasscodeEntry = browser.find_element_by_css_selector("#cppConfirmPassword")
confirmPasscodeEntry.send_keys(GET_old_passcode())

changePasscode = browser.find_element_by_css_selector("#react-root > section > main > div > article > form > div:nth-child(4) > div > div > button")
changePasscode.click()

send_Mail(data)

profileButon = browser.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5)")
profileButon.click()

browser.close()



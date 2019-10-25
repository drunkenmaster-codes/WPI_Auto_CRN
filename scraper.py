#!/usr/bin/python3
from time import sleep
from selenium import webdriver
from getpass import getpass

def openBrowser ():
    driver = webdriver.Chrome("chromedriver")
    driver.get("https://bannerweb.wpi.edu/pls/prod/twbkwbis.P_WWWLogin")
    print("Enter username: ")
    userName = input()
    driver.find_element_by_name("sid").send_keys(userName)
    password = getpass('Enter Password: ')    
    driver.find_element_by_name("PIN").send_keys(password)
    driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()
    sleep(1)
    driver.get("https://bannerweb.wpi.edu/pls/prod/bwskfreg.P_AltPin")
    sleep(1)
    driver.find_element_by_xpath('//input[@type="submit" and @value="Submit"]').click()
    sleep(300)
    driver.quit()
openBrowser()

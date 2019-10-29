#!/usr/bin/python3

from time import sleep
from selenium import webdriver
from getpass import getpass
from os import system, name 
driver = webdriver.Chrome("chromedriver")

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def openBrowser():
    driver.get("https://bannerweb.wpi.edu/pls/prod/twbkwbis.P_WWWLogin")
    
    browserMain()

def browserMain ():    
    while True:
        clear()
        print("Enter username: ")
        userName = input()
        driver.find_element_by_name("sid").send_keys(userName)
        password = getpass('Enter Password: ') 
        driver.find_element_by_name("PIN").send_keys(password)
        driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()
        sidList = len(driver.find_elements_by_name("sid"))
        pinList = len(driver.find_elements_by_name("PIN"))
        sleep(1)        
        if (sidList < 1 and pinList < 1):
            break
    driver.get("https://bannerweb.wpi.edu/pls/prod/bwskfreg.P_AltPin")
    sleep(1)
    driver.find_element_by_xpath('//input[@type="submit" and @value="Submit"]').click()
    sleep(3)
    driver.quit()

def crnEntry():
    '''
    returns a list of all the CRNS that need to be added
    '''
    print("Number of CRNS: ")
    number = int(input())
    crnValue = list()
    for i in range(number):
        print(str(i) + "th CRN: ")
        crnValue.append(int(input()))
    return crnValue


openBrowser()    
          

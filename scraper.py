#!/usr/bin/python3

from time import sleep
from selenium import webdriver
from getpass import getpass
from os import system, name 
import datetime
driver = webdriver.Chrome("chromedriver")
execOne = True
timeToExec = ''


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
    '''
    Login and redirects to correct webpage
    '''

    while True:
        clear()
        print("Enter username: ")
        userName = input()
        driver.find_element_by_name("sid").send_keys(userName)
        password = getpass('Enter Password: ') 
        driver.find_element_by_name("PIN").send_keys(password)
        driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()
        clear()
        print("Trying to login..")                   
        sidList = len(driver.find_elements_by_name("sid"))
        pinList = len(driver.find_elements_by_name("PIN"))
        sleep(1)        
        if (sidList < 1 and pinList < 1):
            break
    print("Succesfully logged in.")
    driver.get("https://bannerweb.wpi.edu/pls/prod/bwskfreg.P_AltPin")
    sleep(1)
    driver.find_element_by_xpath('//input[@type="submit" and @value="Submit"]').click()
    sleep(0.5)
    

def crnEntry():
    '''
    returns a list of all the CRNS that need to be added
    '''
    clear()
    print("Promt to enter CRN")
    crnValue = list()
    print("Add a CRN and press ENTER")
    print("Type 'done' after finishing")
    rawInput = ''
    while True:
        rawInput = input()
        if rawInput == 'done' or rawInput == 'DONE' or rawInput == 'Done':
            break
        else:
            crnValue.append(int(rawInput))        
    return crnValue

def addOnTime():
    global execOne
    global timeToExec
    if execOne == True:
        while True:
            timeToExec = input("Enter time in HH:MM format:")
            try:
                datetime.datetime.strptime(timeToExec,"%H:%M")
                
            except ValueError:
                clear()
                print("Error: Input time properly")
                continue
            else:
                break
                
        execOne = False
        return timeToExec
    elif execOne == False:
        return timeToExec
    

def startOnTime():
    ''' Execute when delta-time = 0 or < 0'''
    localTimeToExec = addOnTime()
    while True:addCRN()
        dateSTR = datetime.datetime.now().strftime("%H:%M")
        if dateSTR == localTimeToExec or \
            int(localTimeToExec[0:localTimeToExec.find(':')-1]) > int(dateSTR[0:dateSTR.find(':')-1]) or \
                (localTimeToExec[0:localTimeToExec.find(':')-1] ==  dateSTR[0:dateSTR.find(':')-1] and \
                    int(localTimeToExec[0:localTimeToExec.find(':')-1]) > int(dateSTR[dateSTR.find(':')+ 1:])):  
            print("The Time has come")

            break
        else:
            print("Sleeping zzzzzzzz.")
            sleep(10)       

def addCRN(crnlist):


#openBrowser()    

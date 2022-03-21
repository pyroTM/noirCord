from webbrowser import GenericBrowser
from selenium import webdriver
from time import sleep
import random
import os
import json
import sys
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from password_generator import PasswordGenerator

driver = uc.Chrome()
pwo = PasswordGenerator()
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

def dot_trick(username):
    emails = list()
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""

        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@gmail.com")
    return emails


if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again!")
else:
    with open("config.json") as file:
        config = json.load(file)


def getToken():
    token = driver.execute_script("(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()")

    return token

def registerAccount():

    gmails = dot_trick(config["email"])

    driver.get("https://discord.com/register")

    wait.until(expected_conditions.presence_of_element_located((By.NAME, 'email')))
    sleep(1)
    driver.find_element_by_name('email').send_keys(random.choice(gmails))
    sleep(1)

    wait.until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
    sleep(1)
    driver.find_element_by_name('username').send_keys('noirBot')

    wait.until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
    sleep(1)
    driver.find_element_by_name('password').send_keys(pwo.generate())
    sleep(1)
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'css-1hwfws3'))) 
    sleep(1)
    driver.find_elements_by_class_name('css-1hwfws3')[0].click()  

    actions.send_keys(str(random.randint(1,12))) 
    sleep(1)
    actions.send_keys(Keys.ENTER)

    actions.send_keys(str(random.randint(1,28))) 

    actions.send_keys(Keys.ENTER)
    sleep(1)
    actions.send_keys(str(random.randint(1990,2001))) 
    sleep(1)
    actions.send_keys(Keys.ENTER)

    actions.send_keys(Keys.TAB) 

    actions.send_keys(Keys.ENTER) 

    actions.perform() 

    wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div')))

    e = str(input("Captcha Solved?: "))

    if e == "y":
        sleep(5)
        getToken()
        sleep(3)
        driver.close()



registerAccount()

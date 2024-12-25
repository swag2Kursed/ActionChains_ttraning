import selenium

import os

from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import pickle

import random

import selenium.webdriver.support.expected_conditions as EC

import time

from selenium.webdriver import Keys

from selenium.webdriver.common.action_chains import ActionChains

wait = WebDriverWait    
browser = webdriver.Chrome()
browser.get("https://demoqa.com/progress-bar")
action = ActionChains(browser)

start = browser.find_element(By. ID, "startStopButton").click()

progress = wait(browser, 15).until(
    EC.text_to_be_present_in_element((By. CLASS_NAME, "progress-bar"), "100%") 
)

reset = browser.find_element(By. ID, "resetButton").click()
time.sleep(4)
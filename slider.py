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
browser.get("https://demoqa.com/slider")
action = ActionChains(browser)

slider_element = browser.find_element(By. CLASS_NAME, "range-slider")

action.drag_and_drop_by_offset(slider_element, 100 , 50)
action.perform()

time.sleep(4)

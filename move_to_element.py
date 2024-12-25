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
browser.get("https://demoqa.com/menu")
action = ActionChains(browser)

main_item = browser.find_elements(By. CSS_SELECTOR, "a[href='#']")[1]
sub_list = browser.find_elements(By. CSS_SELECTOR, "a[href='#']")[4]
action.move_to_element(main_item)
action.move_to_element(sub_list)
action.perform()
time.sleep(5)
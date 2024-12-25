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

wait = WebDriverWait    
browser = webdriver.Chrome()
browser.get("https://hyperskill.org/")

current_tab = browser.current_window_handle
print(current_tab)

lets_go = wait(browser, 10).until(
    EC.presence_of_all_elements_located((By. CLASS_NAME, "w-inline-block"))
)[3].click()
time.sleep(1)

browser.switch_to.window('3EDA625493580872A4C1C187D05C35D7')

pricing = wait(browser, 5).until(
    EC.presence_of_all_elements_located((By. CSS_SELECTOR, "a[class='nav-link']"))
)[1].click()

current_tab = browser.current_window_handle
print(current_tab)


time.sleep(5)
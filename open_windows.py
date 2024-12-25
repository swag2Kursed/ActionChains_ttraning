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
browser.get("https://www.avito.ru/")
avito_tab = browser.current_window_handle
print(avito_tab, "AVITO")
browser.switch_to.new_window()
browser.get("https://hyperskill.org/login")
hype_skill_tab = browser.current_window_handle
print(hype_skill_tab, "HypeSkill")

browser.switch_to.window(avito_tab)
time.sleep(2)

avito_all_categories = wait(browser, 10).until(
    EC.presence_of_element_located((By. CSS_SELECTOR, "button[class='buyer-location-1cwp8pa']"))
).click()
time.sleep(1)

browser.switch_to.window(hype_skill_tab)
time.sleep(1)
pricing_button = wait(browser, 10).until(
    EC.presence_of_all_elements_located((By. CSS_SELECTOR, "a[class='nav-link']"))
)[1].click()
time.sleep(5)
browser.quit()  



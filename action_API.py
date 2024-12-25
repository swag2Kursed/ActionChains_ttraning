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
browser.get("https://tympanus.net/Development/DragDropInteractions/index.html")
action = ActionChains(browser)

browser.find_elements(By. TAG_NAME, "a")[6].click()
# time.sleep(1)
# page_scale = browser.current_window_handle
# print(page_scale, "<<<<<<<<<<<<<<<")
# browser.switch_to.window(page_scale)

source_element = browser.find_elements(By. CLASS_NAME, "drag-me")[2]
target_element = wait(browser, 5).until(
    EC.presence_of_all_elements_located((By. CLASS_NAME, "drop-area__item"))
)[1]

action.click_and_hold(source_element)
action.pause(1)
action.move_to_element(target_element)
action.release()
action.perform()

time.sleep(5)
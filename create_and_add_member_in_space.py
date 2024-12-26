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
browser.get("https://app.staging.sphera.work")
action = ActionChains(browser)
browser.maximize_window()

OWNER_PHONE = "9999999999"
ONE_TIME_CODE = "9999"

browser.delete_all_cookies()

cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)


browser.get("https://app.staging.sphera.work")

HRM_button = wait(browser, 5).until(
    EC.presence_of_element_located((By. CSS_SELECTOR, "[aria-label='Система управления персоналом']"))
).click()

add_member = wait(browser, 10).until(
    EC.presence_of_element_located((By. CSS_SELECTOR, "a[href='/8832B56C/hrm/create-user']"))
).click()

data = wait(browser, 5).until(
    EC.presence_of_element_located((By. ID, "dob"))
).click()

data_1st_december = browser.find_element(By. CSS_SELECTOR, "[aria-label='Choose Sunday, December 1st, 2024']")

action.move_to_element(data_1st_december)
action.click()
action.perform()
try:
    date_check = wait(browser, 5).until(
    EC.text_to_be_present_in_element_value((By. ID, "dob"), "01/12/2024")
    )
except:
    print("NOT PASS<<<<")    
else:
    print("PASS<<<<")


last_name = browser.find_element(By. NAME, "lastName").send_keys("VANVANVAN")
first_name = browser.find_element(By. NAME, "firstName").send_keys("KARKARKAR")
patronymic = browser.find_element(By. NAME, "patronymic").send_keys("VLAMVLAMVLAM")
phone_number_member = browser.find_element(By. ID, "phone").send_keys("9286061337")
email_memer = browser.find_element(By. NAME, "email").send_keys("KarnoCOOLMAN@mail.su")
gender = browser.find_elements(By. NAME, "sex")[0].click() # [1] women

job_title = wait(browser, 10).until(
    EC.element_to_be_clickable((By. CLASS_NAME, "select__dropdown-indicator"))
).click()
time.sleep(1)
QA_job_title = wait(browser, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "select__option"))
)[1]
action.move_to_element(QA_job_title)
action.click()
action.perform()
time.sleep(1)

departament = browser.find_element(By.CLASS_NAME, "css-tlfecz-indicatorContainer").click()
time.sleep(1)
UI_departament = wait(browser, 5).until(
    EC.presence_of_all_elements_located((By. CLASS_NAME, "select__option"))
)[3]
action.move_to_element(UI_departament)
action.click()
action.perform()
time.sleep(1)

supervisor = browser.find_elements(By. CLASS_NAME, "css-tlfecz-indicatorContainer")[1].click()
supervisor_choice = wait(browser, 5).until(
    EC.presence_of_all_elements_located((By. CLASS_NAME, "select__option"))
)[17]
action.move_to_element(supervisor_choice)
action.click()
action.perform()

leader_ship = browser.find_elements(By. CLASS_NAME, "css-tlfecz-indicatorContainer")[-1].click()
leader_choice = wait(browser, 5).until(
    EC.presence_of_all_elements_located((By. CLASS_NAME, "select__option"))
)[3]
action.move_to_element(leader_choice)
action.click()
action.perform()

status_company = browser.find_elements(By. NAME, "status")[1].click()
job_day = browser.find_elements(By. NAME, "workingDay")[1].click()











time.sleep(5)









time.sleep(3)
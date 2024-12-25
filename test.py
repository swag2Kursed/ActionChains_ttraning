
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://staging.sphera.work/")
    page.get_by_placeholder("+7 9XX XXX-XX-XX").click()
    page.get_by_placeholder("+7 9XX XXX-XX-XX").fill(" 999 999-99-99 ")
    page.get_by_role("button", name="Получить код").click()
    page.locator("#one-time-code").fill("9999")
    page.get_by_role("button", name="Войти").click()
    page.get_by_label("Создать канал").click()
    page.locator("#name").click()
    page.locator("#name").fill("мсмллдвпартчв4")
    page.get_by_role("button", name="Продолжить").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)






































# from selenium import webdriver

# import playwright

# from selenium.webdriver.common.by import By

# import time

# from selenium.webdriver.support.ui import WebDriverWait

# import selenium.webdriver.support.expected_conditions as EC

# from selenium.webdriver.common.keys import Keys

# import re
# from playwright.sync_api import Playwright, sync_playwright




# link = "https://staging.sphera.work/"

# browser = webdriver.ChromiumEdge()

# browser.get(link)

# phone_field = WebDriverWait(browser, 10).until(
# EC.presence_of_element_located((By.ID, "phone"))
# )
# phone_field.send_keys("9888888888")

# receive_code_button = browser.find_element(By.CSS_SELECTOR, "button.phone-input__receive-button")
# receive_code_button.click()

# one_time_code_field = WebDriverWait(browser, 10).until(
# EC.presence_of_element_located((By.ID, "one-time-code"))
# )
# one_time_code_field.send_keys('8888')

# submit_code_button = WebDriverWait(browser, 10).until(
# EC.presence_of_element_located((By.XPATH, "//*[@id='root']//div[2]/div[2]//button"))
# )
# submit_code_button.click()









# def run(playwright: Playwright):  

#     browser = playwright.chromium().launch(
#         channel = "chrome",
#         headless = False
#     )
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://staging.sphera.work/")
#     page.get_by_placeholder("+7 9XX XXX-XX-XX").fill("+7 999 999-99-99 ")
#     page.get_by_role("button", name="Получить код").click()
#     page.locator("#one-time-code").fill("9")
#     page.goto("https://staging.sphera.work/workspace/choice?type=signin")
#     page.get_by_role("button", name="Войти").click()


    # time.sleep(10)
    # browser.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

from send import (_login, _password)

_login = _login
_password = _password

url = 'https://visa.vfsglobal.com/blr/ru/pol/login'
driver = webdriver.Firefox(executable_path='/opt/odoo/pets/firefoxdriver/geckodriver')
result_msg = ''

try:
    driver.get(url=url)
    time.sleep(5)
    cookies = driver.find_element(By.XPATH, value='//button[@id="onetrust-reject-all-handler"]')
    cookies.click()
    email_input = driver.find_element(by='id', value='mat-input-0')
    email_input.clear()
    email_input.send_keys(_login)

    pass_input = driver.find_element(by='id', value='mat-input-1')
    pass_input.clear()
    pass_input.send_keys(_password)
    pass_input.send_keys(Keys.ENTER)
    time.sleep(5)

    press_write = driver.find_element(By.XPATH, value='//div[@class="position-relative"]//button')
    time.sleep(1)
    press_write.click()
    time.sleep(1)

    select_center = driver.find_element(By.XPATH, value='//mat-select[@id="mat-select-0"]')
    time.sleep(2)
    select_center.click()
    time.sleep(10)
    select_center.send_keys(Keys.END)
    time.sleep(2)

    center_minsk = driver.find_element(By.XPATH, value='//mat-option[@id="mat-option-5"]')
    time.sleep(10)
    center_minsk.click()
    time.sleep(2)

    select_post_category = driver.find_element(By.XPATH, value='//mat-select[@id="mat-select-2"]')
    time.sleep(2)
    select_post_category.click()
    time.sleep(2)

    select_post_category_detail = driver.find_element(By.XPATH, value='//mat-option[@id="mat-option-11"]')
    time.sleep(2)
    select_post_category_detail.click()
    time.sleep(2)

    select_subcategory = driver.find_element(By.XPATH, value='//mat-select[@id="mat-select-4"]')
    time.sleep(2)
    select_subcategory.click()
    time.sleep(2)

    select_subcategory_detail = driver.find_element(By.XPATH, value='//mat-option[@id="mat-option-16"]')
    time.sleep(2)
    select_subcategory_detail.click()
    time.sleep(2)

    result_msg = driver.find_element(By.XPATH, value='//div[@class="border-info mb-0 ng-star-inserted"]').text
    print(result_msg)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


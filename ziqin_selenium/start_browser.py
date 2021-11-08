#coding=utf-8
from pytesseract.pytesseract import image_to_string
from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://reg.jd.com/p/regPage")

# time.sleep(2)

# locator = (By.CLASS_NAME,"protocol-button")
# WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
# driver.close()

# EC.title_contains("注册")
# pro_button = driver.find_element_by_class_name('protocol-button')
# pro_button.find_element_by_tag_name('button').click()
# driver.find_element_by_id("form-phone").send_keys("17717827665")

for i in range(8):
     user_email = ''.join(random.sample('1234567890abcd',8))+'@163.com'
     print(user_email)
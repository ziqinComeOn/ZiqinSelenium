#coding=utf-8
import time
import random
from selenium import webdriver
from PIL import Image


driver = webdriver.Chrome()
#浏览器初始化
def driver_init():
    driver.get("https://reg.jd.com/p/regPage")
    driver.maximize_window()
    time.sleep(5)

#获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

#获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcd',8))
    return user_info

 #获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("get_code")
    print(code_element.location) #{"x":123,"y":345}
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width']+left
    height = code_element.size['height']+top
    im = Image.open(file_name)
    img = im.crop(left,top,right,height)
    img.save(file_name)


#解析图片获取验证码
def code_online():
    """这里是获取验证码的第三方api"""



#运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+'@163.com'
    file_name = "/Users/simufengyun/Desktop/selenium_project/ziqin_selenium/Image/test01.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("123123")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    get_element('register-btn').click()
    driver.close()

run_main()    


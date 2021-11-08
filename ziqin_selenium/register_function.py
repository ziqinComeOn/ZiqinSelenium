#coding = utf-8
import sys
sys.path.append('/Users/simufengyun/Desktop/selenium_project/ziqin_selenium')
import time
import random
from selenium import webdriver
from PIL import Image
from find_element import FindElement
class RegisterFuction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)

    #获取driver并打开url    
    def get_driver(self,url,i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i==2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver

    #输入用户信心
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)


    #定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element


    #获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcd',8))
        return user_info

    #获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        print(code_element.location) #{"x":123,"y":345}
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        img = im.crop(left,top,right,height)
        img.save(file_name)


    #解析图片获取验证码
    def code_online(self,file_name):
        """这里是获取验证码的第三方api"""
        self.get_code_image()





    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info+"@163.com"
        file_name = "/Users/simufengyun/Desktop/selenium_project/ziqin_selenium/Image/test01.png"
        code_text = self.code_online(file_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name',user_name_info)
        self.send_user_info('password','123456')
        self.send_user_info('code_text',code_text)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element("code_text_error") #获取验证码提示信息是否存在
        if code_error == None:
            print("注册成功")
        else:
            #验证码失败时 截图保留错误证据信息 便于查看错误原因
            self.driver.save_screenshot("/Users/simufengyun/Desktop/selenium_project/ziqin_selenium/Image/codeerror.png")    
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    #循环启动不同浏览器
    for i in range(3):
        register_function = RegisterFuction("https://reg.jd.com/p/regPage",i)
        register_function.main()
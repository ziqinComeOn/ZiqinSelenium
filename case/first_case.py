#coding=utf-8
import sys
from unittest import suite
sys.path.append('/Users/simufengyun/Desktop/selenium_project/ziqin_selenium')
from business.register_business import RegisterBusiness
from selenium import webdriver
import os
import unittest
import HTMLTestRunner
import time
from datetime import datetime
from log.user_log import UserLog

class FirstCase(unittest.TestCase):
    #装饰器
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    #此case先置条件
    def setUp(self):
        #验证码图片截图路径
        self.file_name = "/Users/simufengyun/Desktop/selenium_project/ziqin_selenium/Image/test01.png"
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        # self.logger.debug("this is chrome")
        #日志
        self.logger.info("this is chrome")
        
        self.login = RegisterBusiness(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    #此case后置条件
    def tearDown(self):
        time.sleep(2)
        #封装错误截图处理
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                now_times = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                base_dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                file_path = file_path = os.path.join(base_dirs+'/report/image/'+case_name+'_'+now_times+".png")
                self.driver.save_screenshot(file_path) #截图
        self.driver.close()

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34','user111','11111',self.file_name)
        # if email_error == True:
        #     print("注册成功了，此条case执行失败")
        #通过 断言assert判断是否为error
        self.assertFalse(email_error,'测试失败')

    def test_login_username_error(self):
        username_error = self.login.login_name_error('34','user111','11111',self.file_name)
        #断言 assertFalse
        self.assertFalse(username_error)
          
    def test_login_password_error(self):
        password_error = self.login.login_password_error('34','user111','11111',self.file_name)
        self.assertFalse(password_error)

    def test_login_code_error(self):
        code_error = self.login.login_code_error('34','user111','11111',self.file_name)
        self.assertFalse(code_error)

    def test_login_success(self):
        success = self.login.user_base('34','user111','11111',self.file_name)
        self.assertFalse(success)           

'''
def main():
    first = FirstCase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_success()
'''

if __name__ == '__main__':
    now_time = datetime.now().strftime("%Y-%m-%d %H-%M")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir+'/report/'+'first_case_'+now_time+'.html')
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_code_error'))
    # suite.addTest(FirstCase('test_login_username_error'))
    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='This is first report',description="这个是我们第一次测试报告",verbosity=2)
    runner.run(suite)
#coding = utf-8
import sys
sys.path.append('/Users/simufengyun/Desktop/selenium_project/ziqin_selenium')
from business.register_business import RegisterBusiness
from selenium import webdriver
from unittest import suite
import os
import unittest
import HTMLTestRunner
from util.excel_util import ExcelUtil
import time
from datetime import datetime
import ddt
ex = ExcelUtil()
data = ex.get_data() #拿到excel里的数据
@ddt.ddt
#邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
class FirstDdtCase(unittest.TestCase):
    #此case先置条件
    def setUp(self):
        #验证码图片截图路径
        self.file_name = "/Users/simufengyun/Desktop/selenium_project/ziqin_selenium/Image/test01.png"
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.login = RegisterBusiness(self.driver)

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
    
    # @ddt.data(
    #     # ['email','username','password','code','assertCode','assertText']
    #     ['12','Ziqin','111111','code','user_email_error','请输入有效的电子邮件地址'],
    #     ['@qq.com','Ziqin','111111','code','user_email_error','请输入有效的电子邮件地址'],
    #     ['1234@qq.com','Ziqin','111111','code','user_email_error','请输入有效的电子邮件地址']
    # )
    # @ddt.unpack

    # def test_register_case(self,email,username,password,code,assertCode,assertText):
    #     email_error = self.login.register_function(email,username,password,code,assertCode,assertText)
    #     #通过 断言assert判断是否为error
    #     self.assertFalse(email_error,'测试失败')

    #拿到excel表格里的数据
    @ddt.data(*data)

    def test_register_case(self,data):
        email,username,password,code,assertCode,assertText = data #list赋值
        email_error = self.login.register_function(email,username,password,code,assertCode,assertText)
        #通过 断言assert判断是否为error
        self.assertFalse(email_error,'测试失败')

if __name__ == '__main__':
    now_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    #根目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(base_dir)
    file_path = os.path.join(base_dir+'/report/'+'first_case1_'+now_time+'.html') 
    # print("我是存储路径",file_path)
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='This is first report1',description="这个是我们第一次测试报告",verbosity=2)
    runner.run(suite)
    

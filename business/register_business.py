#coding=utf-8
from handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    def __init__(self,driver):
        #实例化
        self.register_h = RegisterHandle(driver) 
    #
    def user_base(self,email,name,password,file_name):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(file_name)
        self.register_h.click_register_button()
    
    def register_success(self):
        if self.register_h.get_register_text() == None:
            return True
        else:
            return False    

    # 执行操作handle层
    def login_email_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('user_email_error',"请输入有效的电子邮件地址") == None:
            print("邮箱验证不成功")
            return True
        else:
            return False 

    #通用方法
    def register_function(self,email,name,password,file_name,assertCode,assertText):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text(assertCode,assertText) == None:
            # print("邮箱验证不成功")
            return True
        else:
            return False  

    #name错误
    def login_name_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('user_name_error',"字符长度必须大于等于4，小于等于8位") == None:
            print("用户名校验不成功")
            return True
        else:
            return False            
    #password错误
    def login_password_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('password_error',"密码长度大于5") == None:
            print("密码校验不成功")
            return True
        else:
            return False    

    def login_code_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('code_text_error',"验证码错误") == None:
            print("验证码校验不成功")
            return True
        else:
            return False                    
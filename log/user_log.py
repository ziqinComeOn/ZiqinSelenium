#coding=utf-8
import logging
import os
import datetime
class UserLog(object):
    def __init__(self):
        #实例化日志类 赋值给logger 并全局化
        self.logger = logging.getLogger()
        #设置输出日志等级
        self.logger.setLevel(logging.DEBUG)


        #文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        #拼接日志文件存放路径
        log_dir = os.path.join(base_dir,"logs")
        #日志按时间命名
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        #拼接日志文件路径
        log_name = log_dir+'/'+log_file

        #文件输出日志
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s --> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

       


    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

            
if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('test1')
    user.close_handle()
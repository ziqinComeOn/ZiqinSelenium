#coding=utf-8
import os
import unittest
class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path1 = os.path.join(os.getcwd(),'case') #有时找不到
        print('我是目录',case_path1) #我是目录 /Users/simufengyun/Desktop/selenium_project/case
        #找到要执行的文件所在根目录
        case_path = os.path.join(os.path.dirname(os.path.abspath('case')))
        print('我是根目录',case_path) #我是根目录 /Users/simufengyun/Desktop/selenium_project
        #此处重点关注路径问题，有时可能没找对，需要拼接
        base_dir = os.path.join(case_path,'ziqin_selenium/case')
        print(base_dir)
        suite = unittest.defaultTestLoader.discover(base_dir,'unittest_*.py')
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()
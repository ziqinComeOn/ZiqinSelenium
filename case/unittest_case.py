#coding=utf-8
import unittest

# from ziqin_selenium.case.first_case import FirstCase
class FirstCase01(unittest.TestCase):

    #装饰器 
    @classmethod
    def setUpClass(cls):
        print("这个是case的前置条件")

    @classmethod
    def tearDownClass(cls):
        print("这个是case的前置条件")

    def setUp(self):
        print("这个是case的前置条件")
    
    def tearDown(self):
        print("这个是case的后置条件")

    @unittest.skip('不执行第一条')
    def testfirst01(self):
        print("第一条case")

    def testfirst02(self):
        print("第二条case")
    
    def testfirst03(self):
        print("第3条case")

if __name__ == '__main__':
    # unittest.main()    
    suite = unittest.TestSuite()    
    suite.addTest(FirstCase01('testfrst02')) #添加要执行的case
    suite.addTest(FirstCase01('testfrst01')) #添加要执行的case
    unittest.TextTestRunner().run(suite)
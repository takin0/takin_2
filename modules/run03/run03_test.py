#coding=utf-8
import sys,os,unittest
path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
sys.path.append(path_load_ini)
from modules.mains.log import takin_log
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By

#from modules.run03.run03_procs import Run03bro
from modules.run03.run03unit import  MyTest

from modules.run03.element_run03 import *
from BeautifulReport import BeautifulReport

class loginTest(MyTest):
    
    def save_img(self,img_name):
        self.run03bro.get_screenshot_as_file(img_name)

    @takin_log("登录测试")   
    @BeautifulReport.add_test_img("test_correct_login")
    def test_correct_login(self):
        
        '''正确登录测试'''
        login_info = self.run03bro.login("superadmin","P@ssw0rd",denglu_info_sucess)
        #text=u"获取信息失败"
        #ts=self.run03bro.xinxi()
        #self.assertEqual(ts, text)
        self.assertTrue(login_info)

    @takin_log("创建项目")
    @BeautifulReport.add_test_img("test_create_pjt")
    def test_create_pjt(self):
        '''部署项目测试'''        
        self.run03bro.create_pjt()
        

"""
    def test_usererr_login(self):
        
        '''账号错误登录测试'''
        login_info = self.run03bro.login("supera","P@ssw0rd",denglu_info_fail)
        self.assertTrue(login_info)
        #text=u"用户名或者密码不正确！"
        #ts=self.yanbro.xinxi()
        #self.assertEqual(ts, text)

    def test_passerr_login(self):
        
        '''密码错误登录测试'''
        login_info = self.run03bro.login("superadmin","P#ssw0rd",denglu_info_fail)
        self.assertTrue(login_info)
        #text=u"用户名或者密码不正确！"
        #ts=self.yanbro.xinxi()
        #self.assertEqual(ts, text)
"""

if __name__=='__main__':
    #a=loginTest()
    unittest.main(exit=True)

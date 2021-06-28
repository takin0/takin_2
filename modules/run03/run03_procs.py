#coding=utf-8 
from os import path as opath
from sys import path as spath
#配置路径model到环境
path_load_ini=opath.dirname(opath.dirname(opath.dirname(opath.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
spath.append(path_load_ini)

from modules.mains.log import takin_log
from modules.mains.browser import Browser
from modules.run03.element_run03 import *

testurl="https://10.10.11.7:9004"
testname="quanju"
testwd="P@ssw0rd"

class Run03bro(Browser):
    @takin_log("登录")
    def login(self,testname,testwd,denglu_info,remb="T"):
        super().open_url(testurl)
        super().olwt(10)
        super().em_input(username_css,testname)
        super().em_input(password_css,testwd)
        super().sleep(2)
        if remb=="T":     
            super().em_click(rember_css)
        super().em_click(login_xpath)
        info = super().duanyan(denglu_info_xpath,denglu_info)
        return info

    @takin_log("创建项目")
    def create_pjt(self):
        super().em_click(pjt_css)
        super().em_click(cre_pjt_css)
        super().em_input(pjt_name_css,testname)
        super().sleep(2)
        super().em_input(pjt_path_css,testname)
        super().sleep(2)
        
        super().em_input(pjt_file_xpath,pjt_file_name)
        super().sleep(2)
        super().em_click(pjt_create_xpath)
        super().sleep(12)
        super().olwt(10)

    @takin_log("登出")
    def logout(self,confirm=""):
        super().sleep(2)
        super().em_click(logout_css)
        super().sleep(2)
        if confirm:
            super().em_click(quxiao_xpath)
        else:
            super().em_click(queding_xpath)

    @takin_log("登录提示")
    def xinxi(self):
        try:
            super().olwt(10)
            super().sleep(2)
            a = super().em_text(em_all='/html/body/div[2]/div/div/div[1]/div/span')
            return a
        except:
            return "获取信息失败"
              
if __name__ == "__main__":

        testname="superadmin"
        testwd="P@ssw0rd"
        yb=Run03bro()
        a=yb.login(testname,testwd,"用户名或者密码不正确！")
        yb.create_pjt()



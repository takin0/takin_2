#coding=utf-8 
from os import path as opath
from sys import path as spath
#配置路径model到环境
path_load_ini=opath.dirname(opath.dirname(opath.dirname(opath.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
spath.append(path_load_ini)

from modules.mains.log import takin_log
from modules.mains.browser import Browser
from modules.run04.element_run04 import *

testurl="https://10.10.11.4:9004"
testname="quanju"
testwd="P@ssw0rd"

class Run04bro(Browser):
        
    @takin_log("登录失败")
    def login(self,testname,testwd,remb=""):
        super().open_url(testurl)
        super().olwt(10)
        super().by_css(username_css)
        super().clear()
        super().input(testname)
        super().by_css(password_css)
        super().clear()
        super().input(testwd)
        super().sleep(2)
        super().by_verifi(verifiipt_xpath)
        if remb=="T":     
            zz=super().by_css(rember_css)
            super().click()
        login=super().by_xpath(login_xpath)
        super().click()
    
    def logout(self,confirm=""):
        time.sleep(2)
        super().by_css(logout_css)
        super().click()
        time.sleep(2)
        if confirm:
            cfm=confirm
            quxiao=super().by_xpath(quxiao_xpath)
            super().click()
        else:
            queding=super().by_xpath(queding_xpath)
            super().click()
    def xinxi(self):
        try:
            super().olwt(10)
            #time.sleep(2)
            super().by_xpath(login_mes_xpath)
            a=super().text()
            return a
        except:
            return "获取信息失败"
             
if __name__ == "__main__":

        testname="superadmin"
        testwd="P@ssw0rd"
        yb=Run04bro()
        ss=Run04bro()
        yb.login(testname,testwd,"T")
        ss.login("quanju",testwd,"T")
        yb.logout()



#coding=utf-8 
import os,sys,time#,logging

#配置路径model到环境
path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
sys.path.append(path_load_ini)

from modules.mains.log import takin_log
from modules.mains.browser import Browser
from modules.gp02.element_gp02 import *



class Gp02bro(Browser):
      

    def login(self,testname,testwd,remb=""):
        super().olwt(10)
        super().max()
        super().em_input(username_xpath,testname)
        super().em_input(password_xpath,testwd)
        time.sleep(2)
        if remb=="T":     
            zz=super().em_click(rember_xpath)
        login=super().em_click(login_xpath)
        #info = super().duanyan(denglu_info_xpath,denglu_info)
        #return info

    #圈选
    def start_qx(self,pj_name,url):
        
        time.sleep(2)
        super().em_click(work_xpath)
        super().olwt(10)
        super().em_click(my_project_xpath)
        super().olwt(10)
        super().em_click(create_project_xpath)
        super().olwt(10)
        super().em_input(project_name_xpath,pj_name)
        super().olwt(10)
        super().em_click(sure_xpath)
        super().olwt(10)
        super().em_input(url_xpath,url)
        super().olwt(10)
        super().em_click(start_xpath)
        
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

        testname="zhang"
        testwd="qq111111"
        yb=Gp02bro
        yb.login(testname,testwd,"T")
        yb.start_qx("xxx","www.baidu.com")
        #yb.logout()




#coding=utf-8 
#定义浏览器的类，包括浏览器打开、最大化、刷新、前进、后退、新标签、关闭等
import sys,os,datetime,time
import requests

path_base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base=path_base.replace('\\', '/')
sys.path.append(path_base)

from modules.mains.log import takin_log

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from modules.mains import global_dict as gd
from modules.mains.load_ini import ReadConfig
from modules.mains.send_verifi_mail  import  send_verifi_mail
from modules.mains.get_verifi_mail  import  get_verifi_mail



class Browser():
        brscf = ReadConfig()
        chrome_browser_path = brscf.get_brscf("chrome_browser_path")
        chrome_driver_path = brscf.get_brscf("chrome_driver_path")
        chrome_browser_kernel = brscf.get_brscf("chrome_browser_kernel")
        
        #@takin_log("init浏览器失败")
        def __init__(self,browser_path=chrome_browser_path,driver_path=chrome_driver_path,browser_kernel=chrome_browser_kernel):
                
                options = eval("webdriver."+browser_kernel.title()+"Options()")
                options.add_argument('--no-sandbox')
                options.add_argument('--ignore-certificate-errors')#跳过禁用
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                options.binary_location = browser_path                
                self.dr = eval("webdriver."+browser_kernel.title()+"(executable_path = driver_path,options = options)")
                #self.dr = eval("webdriver."+browser_kernel.title()+"(driver_path)")
#2最大化
        @takin_log("最大化窗口失败")
        def max(self,xnm = '',ynm = ''):
                if xnm and ynm:
                        self.dr.set_window_size(xnm,ynm)
                else:
                        self.dr.maximize_window()
                        
        def get_screenshot_as_file(self,path):
                print(path)
                self.dr.get_screenshot_as_file(path)

#0打开网址
        @takin_log("打开网址失败，请检查URL")
        def open_url(self,urls):
                try:
                    self.dr.get(urls)
                except:
                    info = "打开网址失败，请检查URL"
                    self.create_img (info)
                    print(info)
#截图
        @takin_log("创建截图失败")
        def create_img (self,img_name):
                report_path = gd.get_global('report_path')
                #print(report_path)
                img_path = report_path + "\\image\\"
                if os.path.isdir(img_path):
                        path_img = img_path + img_name + ".png"
                        img = self.dr.save_screenshot(path_img)
                        print("图片保存在" + path_img)
                        return path_img
                else:
                        print('图片保存路径{}不存在'.format(img_path))
#2后退
        @takin_log("后退失败")
        def back(self):
                self.dr.back()
#2前进
        def forward(self):
                self.dr.forward()
#2刷新
        def refresh(self):
                self.dr.refresh()
#2关闭网页
        def close(self):
                self.dr.close()
#1关闭浏览器
        def quit(self):
                self.dr.quit()
#2调用JS
        def jsc(self,js):
                self.dr.execute_script(js)
#2新的tab页
        def newtable(self,url):
                JS = 'window.open("{}");'.format(url)#在字符串中引用变量
                self.dr.execute_script(JS)
#2滑动滚动条某一像素
        def bottom(self,ypxs,xpxs = ''):
                if xpxs:
                        JS = "window.scrollTo('{}','{}')".format(xpxs,ypxs)
                        self.dr.execute_script(JS)
                else:
                        JS = "window.scrollTo(0,'{}')".format(ypxs)
                        self.dr.execute_script(JS)

#2获取cookies                
        def getcook(self,keys = ""):
                if keys:
                        cook = self.dr.get_cookie(keys)
                        print(cook)
                else:
                        cook = self.dr.get_cookies()
                        print(cook)
                return cook
#2添加cookies
        def addcook(self,zidian):
                self.dr.add_cookie(zidian)
                #示例 addcook({"name":"testname_1234567890","value":"testvalue_1234567890"})
#3删除cookies
        def delcook(self,name = ''):
                if name:
                        self.dr.delete_cookie(name)
                else:
                        self.dr.delete_all_cookies()
#1通过id定位
        def by_id(self,em_id,img_info=str(time.time())):
                try:
                    self.em = self.dr.ind_element_by_id(em_id)
                except:
                    info = "未找到id为{}的元素".format(em_id)
                    self.create_img (img_info)
                    print(info)
#0通过xpath定位
        #@takin_log("未找到xpath元素")
        def by_xpath(self,em_xpath,logout='',img_info=str(time.time())):
                if logout:
                    try:
                        self.em = self.dr.find_element_by_xpath(em_xpath)
                    except:
                                info = "未找到xpath为{}的元素".format(em_xpath)
                                self.create_img (img_info)
                                print(info)
                                return False
                else:
                        try:
                                self.em = self.dr.find_element_by_xpath(em_xpath)
                        except:
                                info = "未找到xpath为{}的元素".format(em_xpath)
                                self.create_img (img_info)
                                print(info)
                                return False

        def by_verifi(self,vrf_xpath,inpt_xpath,n=4):
  
                mail_key = gd.get_global('mail_key')
                path_img = self.create_img ("verificode")
                time.sleep(1)
                #print(mail_key+"?"+path_img)
                mail_key = 'Verification Code_'+mail_key
                send_verifi_mail(path_img,mail_key)                
                verifi = get_verifi_mail(n,mail_key)
                inpt = self.dr.find_element_by_xpath(inpt_xpath)
                inpt.send_keys(verifi)

                        
#0通过css选择器定位
        def by_css(self,em_css,img_info=str(time.time())):
                try:
                    self.em = self.dr.find_element_by_css_selector(em_css)
                except:
                    info = "未找到css选择器为{}的元素".format(em_css)
                    self.create_img (img_info)
                    print(info)
                    
#1通过链接的关键字定位链接
        def by_link(self,em_text,Q = '',img_info=str(time.time())):
                if Q:
                        try:
                            Q = 'Q'    
                            
                            self.em = self.dr.find_element_by_link_text(em_text)
                        except:
                            info = "未找到关键字为{}的元素".format(em_text)
                            self.create_img (img_info)
                            print(info)  
                else:
                        try:
                            self.em = self.dr.find_element_by_partial_link_text(em_text)
                        except:
                            info = "未找到关键字为{}的元素".format(em_text)
                            self.create_img (img_info)
                            print(info)
                            
#1将xpath和css选择器合并
        def by_all(self,em_all,img_info=str(time.time())):
                try:
                        if '/' in em_all :
                                self.em = self.dr.find_element_by_xpath(em_all)
                        else:
                                self.em = self.dr.find_element_by_css_selector(em_all)

                except:
                       info = "by_all函数未找元素:{}".format(em_all)
                       self.create_img (img_info)
                       print(info)
                #return em_all

        def em_click(self,em_all,img_info=str(time.time())):
                try:
                        if '/' in em_all :
                                self.em = self.dr.find_element_by_xpath(em_all)
                        else:
                                self.em = self.dr.find_element_by_css_selector(em_all)
                        self.em.click()

                except:
                       info = "em_click函数未找元素:{}".format(em_all)
                       self.create_img (img_info)
                       print(info)
                       
        def em_input(self,em_all,shuju='',img_info=str(time.time())):
                try:
                        if '/' in em_all :
                                self.em = self.dr.find_element_by_xpath(em_all)
                        else:
                                self.em = self.dr.find_element_by_css_selector(em_all)
                        self.em.clear()
                        self.em.send_keys(shuju)

                except:
                       info = "em_input函数未找元素:{}".format(em_all)
                       self.create_img (img_info)
                       #print(info)
                       
        def em_text(self,em_all,img_info=str(time.time())):
                try:
                        if '/' in em_all :
                                self.em = self.dr.find_element_by_xpath(em_all)
                        else:
                                self.em = self.dr.find_element_by_css_selector(em_all)
                        info = self.em.get_attribute("textContent")
                        #print(info)
                        return info

                except:
                        info = "em_text函数未找元素:{}".format(em_all)
                        self.create_img (img_info)
                        print(info)              
#1清除内容
        def clear(self):
                try:
                        self.em.clear()
                except:
                        info = "元素不能删除信息"
                        self.create_img (info)
                        print(info)
#0输入数据
        def input(self,shuju = ""):
                if shuju:
                        shuju = shuju
                else:
                        shuju = ""
                self.em.send_keys(shuju)
#0点击元素
        def click(self):
                self.em.click()
#1获取属性
        def attri(self,attr):
                info = self.em.get_attribute(attr)
                #print(info)
                return info
#1获取信息                
        def text(self):
                info = self.em.get_attribute("textContent")
                #print(info)
                return info
        
        def sleep(self,n):
                time.sleep(n)
#0隐式等待               
        def olwt(self,_second = ""):
                if _second:
                        _second = _second
                else:
                        _second = 7
                self.dr.implicitly_wait(_second)
                
#断言 判断元素文本                
        def duanyan(self,em_all,text):
                em_txt = self.em_text(em_all,"断言截图")
                if em_txt == text:
                        return True
                else:
                        #self.create_img (text)
                        return False
#1鼠标单击
        def click_mouse(self,ems = ''):
                if ems: 
                        if '/'in ems:
                                eb = self.dr.find_element_by_xpath(ems)
                                ActionChains(self.dr).click(eb).perform()         
                        else:
                                eb = self.dr.find_element_by_css_selector(ems)
                                ActionChains(self.dr).click(eb).perform()      
                else:
                        ActionChains(self.dr).click().perform()
                        
#1鼠标右键单击
        def rclick_mouse(self,ems = ''):
                if ems:                        
                        if '/'in ems:
                                eb = self.dr.find_element_by_xpath(ems)
                                ActionChains(self.dr).context_click(eb).perform()
                                
                        else:
                                eb =self.dr.find_element_by_css_selector(ems)
                                ActionChains(self.dr).context_click(eb).perform()                    
                else:
                        ActionChains(self.dr).context_click().perform()
                        
#1鼠标移动到某元素
        def move_mouse(self,ems = ''):
                if '/'in ems:
                        eb = self.dr.find_element_by_xpath(ems)
                        ActionChains(self.dr).move_to_element(eb).perform()
                                
                else:
                        eb = self.dr.find_element_by_css_selector(ems)
                        ActionChains(self.dr).move_to_element(eb).perform()
                        
#鼠标移动到某坐标
        def move_zb(self,xzb,yzb):
                ActionChains(self.dr).move_by_offset(xzb,yzb).perform()
                
#移动某元素到某坐标（错误）
        def move_(self,ems,xzb,yzb):
                ActionChains(self.dr).move_to_element_with_offset(ems,xzb,yzb).perform()
#2鼠标双击
        def dclick_elem(self,ems = ''):

                if ems:                        
                        if '/'in ems:
                                eb = self.dr.find_element_by_xpath(ems)
                                ActionChains(dr).double_click(eb).perform()
                                
                        else:
                                eb = self.dr.find_element_by_css_selector(ems)
                                ActionChains(self.dr).double_click(eb).perform()
                        
                else:
                        ActionChains(self.dr).double_click().perform()
                        
#拖动某一元素（未验证）
        def drag_drop(self,fr,to):
                ActionChains(self.dr).drag_and_drop(fr,to).perform()

#单击不松开
        def click_hold(self,ems = ''):
                if ems:
                        if '/'in ems:
                                eb = self.dr.find_element_by_xpath(ems)
                                ActionChains(self.dr).click_and_hold(eb).perform()
                                
                        else:
                                eb = self.dr.find_element_by_css_selector(ems)
                                ActionChains(self.dr).click_and_hold(eb).perform()
                        
                else:
                        ActionChains(self.dr).click_and_hold().perform()
                        
#释放左键
        def release(self):
                ActionChains(self.dr).release().perform()
                
#键盘按键（未完成）
        def key_board(self,key1='',key2 = ''):
                ActionChains(self.dr).key_down(key1).send_keys(key2).key_up().perform()


        def creat_chrome():
                
                creat_chrome = Browser("chrome","Chrome")
                return Browser
#chrome = Browser("chrome","Chrome")
#browser = Browser()

if __name__ == "__main__":
        #browser = Browser("")
        #b=browser
        c=Browser()
        #c=Browser(browser_path="F:\QQDownload\YancloudDaasGenplatform.exe",driver_path="F:\pythonI\\takin-master\driver\chromedriver_90.exe",browser_kernel="chrome")
        #c.open_url("https://10.10.11.4:9004/#/login")
        #c.duanyan()
        #c.by_verifi("/html/body/div/div/div[1]/form/div[3]/div/img","/html/body/div/div/div[1]/form/div[3]/div/div[1]/input")
        #b.max()
        #b.sleep(3)
        #b.key_board("Keys.CONTROL","a")

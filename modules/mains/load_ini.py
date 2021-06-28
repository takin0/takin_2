#coding=utf-8 
#读取加载配置文件global.ini
#读取配置文件的路径
from os import path as opath
from sys import path as spath
path_base = opath.dirname(opath.dirname(opath.dirname(opath.realpath(__file__))))
path_base = path_base.replace('\\', '/')
spath.append(path_base)
from modules.mains.log import takin_log

path_load_ini = opath.dirname(opath.dirname(opath.dirname(opath.realpath(__file__))))+"/conf/"
path_load_ini = path_load_ini.replace('\\', '/')
from  configparser import ConfigParser

class ReadConfig:
    @takin_log("读取配置文件init函数错误")
    def __init__(self,filepath = path_load_ini + "global.ini"):
    
        self.cfgp = ConfigParser()
        self.cfgp.read(filepath)

    @takin_log("get_sections函数错误")
    def get_sections(self):
        section = self.cfgp.sections()
        return section

    @takin_log("get_options函数错误")
    def get_options(self,section):
        options = self.cfgp.options(section)
        return options

    @takin_log("获取浏览器配置get_brscf函数错误")
    def get_brscf(self,param):
        value = self.cfgp.get("browser",param)
        return value

    @takin_log("获取邮箱配置get_emcf函数错误")
    def get_emcf(self,param):
        value = self.cfgp.get("email",param)
        return value
        
if __name__ == '__main__':
    #test = ReadConfig()
    #t = test.get_brscf("browser_path")
    print("t")


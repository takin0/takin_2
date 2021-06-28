#coding=utf-8 
from os import path as opath
from sys import path as spath
#配置路径model到环境
path_load_ini=opath.dirname(opath.dirname(opath.dirname(opath.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
spath.append(path_load_ini)
from unittest import TestCase
from modules.run03.run03_procs import Run03bro

class MyTest(TestCase):
    
    @classmethod
    def setUpClass(self):
        self.run03bro=Run03bro()

    @classmethod
    def tearDownClass(self):
        self.run03bro.quit()



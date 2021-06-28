#coding=utf-8 
from os import path as opath
from sys import path as spath
#配置路径model到环境
path_load_ini=opath.dirname(opath.dirname(opath.dirname(opath.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
spath.append(path_load_ini)
from unittest import TestCase
from modules.run04.run04_procs import Run04bro

class Run04Test(TestCase):
    @classmethod
    def setUpClass(self):
        self.run04bro=Run04bro()
    @classmethod
    def tearDownClass(self):
        self.run04bro.quit()

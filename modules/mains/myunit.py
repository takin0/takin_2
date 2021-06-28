#coding=utf-8 
from os import path as opath
from sys import path as spath
from  unittest import TestCase
path_load_ini=opath.dirname(opath.dirname(opath.dirname(opath.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
spath.append(path_load_ini)

class MyTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
     
    @classmethod
    def tearDownClass(cls):
        pass


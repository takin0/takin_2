#coding=utf-8 
import unittest,os,sys
path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
sys.path.append(path_load_ini)


class MyTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
     
    @classmethod
    def tearDownClass(cls):
        pass


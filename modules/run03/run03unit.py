#coding=utf-8 
import os,sys,unittest#,time

path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
sys.path.append(path_load_ini)
from modules.mains import log
from modules.run03.run03_procs import Run03bro


class MyTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.run03bro=Run03bro()

        
    @classmethod
    def tearDownClass(self):
        self.run03bro.quit()



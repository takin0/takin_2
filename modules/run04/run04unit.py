#coding=utf-8 
import os,sys,unittest
path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\','/')
sys.path.append(path_load_ini)

from modules.run04.run04_procs import Run04bro

class Run04Test(unittest.TestCase):   
    @classmethod
    def setUpClass(self):
        self.run04bro=Run04bro()
    @classmethod
    def tearDownClass(self):
        self.run04bro.quit()

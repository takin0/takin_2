#coding=utf-8 
import os,sys,unittest
path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\','/')
sys.path.append(path_load_ini)

from modules.gp02.gp02_procs import Gp02bro

class Gp02Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.gp02bro=Gp02bro(browser_path="F:\QQDownload\YancloudDaasGenplatform.exe",driver_path="F:\pythonI\\takin-master\driver\chromedriver_84.exe",browser_kernel="chrome")
        
    @classmethod
    def tearDownClass(self):
        self.gp02bro.quit()

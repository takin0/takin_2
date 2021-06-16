#coding=utf-8
import sys,os,unittest
path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
sys.path.append(path_load_ini)

from modules.gp02.gp02unit import Gp02Test
from modules.gp02.gp02_procs import  Gp02bro


class loginTest(Gp02Test):
    def test_correct_login(self):
        
        self.gp02bro.login("superadmin","P@ssw0rd")
        ts=self.gp02bro.start_qx("xxx","www.baidu.com")

if __name__=='__main__':
    unittest.main()

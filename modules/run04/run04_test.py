#coding=utf-8
import sys,os,unittest
path_load_ini=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_load_ini=path_load_ini.replace('\\', '/')
sys.path.append(path_load_ini)

from modules.run04.run04unit import Run04Test
from modules.run04.run04_procs import  Run04bro


class loginTest(Run04Test):
    def test_correct_login(self):
        self.run04bro.login("superadmin","P@ssw0rd")
        text=u"登录成功"
        ts=self.run04bro.xinxi()
        #xdata.quit()
        '''
        if text==ts:
            pass
        else:
            browser.create_img(sys._getframe().f_code.co_name)
        '''
        aaa = self.assertEqual(ts, text)

'''
    #@unittest.skipIf(3 > 2, "登录失败，此用例不执行")
    def test_usererr_login(self):
        xdata.login("supera","P@ssw0rd")
        
        text=u"用户名或密码不正确！"
        ts=xdata.xinxi()
        self.assertEqual(ts, text)

    def test_passerr_login(self):
        xdata.login("superadmin","P#ssw0rd")
        
        text=u"用户名或密码不正确！"
        ts=xdata.xinxi()
        self.assertEqual(ts, text)
'''
if __name__=='__main__':
    unittest.main()

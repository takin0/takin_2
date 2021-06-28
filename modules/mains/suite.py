from os import path as opath
from sys import path as spath
from os import getcwd
from time import sleep
from unittest import TestSuite,defaultTestLoader

base_dir=opath.dirname(opath.dirname(opath.dirname(opath.realpath(__file__))))
base_dir=base_dir.replace('\\', '/')
spath.append(base_dir)
from modules.mains.log import takin_log
from modules.mains.report import TestReport
from modules.mains import sendemail
from modules.mains import global_dict as gd
from BeautifulReport import BeautifulReport as bfr
from modules.mains.sjzfc import sjzf

test_file = "*test.py"
top_level_dir = getcwd()

class Suite():

    @takin_log("创建测试套件")
    def creat_suite(self,test_dir,test_file = test_file):
        suite = TestSuite()
        discover = defaultTestLoader.discover(test_dir, pattern = test_file,top_level_dir = top_level_dir)
        for test_suite in discover:
            for test_case in test_suite:
                suite.addTest(test_case)
        #bfra.report(filename=rep_path+"/test",description='这个描述参数是必填的')
        return suite

    #@takin_log("运行测试套件")不注释会导致beautiful库线程混乱
    def run_suite(self,test_dir,test_file = test_file,description = u"自动化测试报告"):
        sign = test_dir.split("/")[-1]
        r_report = TestReport().creat_report(sign)
        gd._init()
        mail_key = sjzf()
        #print(mail_key)
        sleep(1)
        gd.set_global('report_path',r_report[1])
        sleep(1)
        gd.set_global('mail_key',mail_key)
        aaas="report/{}/report".format(r_report[2])
        #print(gd)
        cccc=bfr(self.creat_suite(test_dir,test_file = test_file))
        cccc.report(filename=aaas,description=description)
        sendemail.send_mail(r_report[1])
'''
        with open(r_report[0], 'w', encoding='utf-8') as file:
            runner = unittest.TextTestRunner(stream = file, descriptions = description, verbosity = 2)   
            runner.run(self.creat_suite(test_dir,test_file = test_file))
        sendemail.send_mail(r_report[1])
'''
        
        
if __name__ == '__main__':
    test_dir = base_dir + "/modules/yancloud"    
    #creat_suite(test_dir)
    suite = Suite()
    suite.run_suite(test_dir)

import sys,os,time,unittest

base_dir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
base_dir=base_dir.replace('\\', '/')
sys.path.append(base_dir)
#import HTMLTestRunner
from modules.mains import log
from modules.mains.report import TestReport
from modules.mains import sendemail
from modules.mains import global_dict as gd
from BeautifulReport import BeautifulReport as bfr
test_file = "*test.py"
top_level_dir = os.getcwd()
from modules.mains.sjzfc import sjzf

#global r_report
class Suite():
    def creat_suite(self,test_dir,test_file = test_file):
        suite = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(test_dir, pattern = test_file,top_level_dir = top_level_dir)
        for test_suite in discover:
            for test_case in test_suite:
                suite.addTest(test_case)

        #bfra.report(filename=rep_path+"/test",description='这个描述参数是必填的')
        return suite

    def run_suite(self,test_dir,test_file = test_file,description = u"自动化测试报告"):
        sign = test_dir.split("/")[-1]
        r_report = TestReport().creat_report(sign)
        gd._init()
        mail_key = sjzf()
        #print(mail_key)
        time.sleep(1)
        gd.set_global('report_path',r_report[1])
        time.sleep(1)
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

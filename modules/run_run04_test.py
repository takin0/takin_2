#coding=utf-8
import sys,os#,time,unittest

base_dir=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
base_dir=base_dir.replace('\\', '/')
sys.path.append(base_dir)
#print(base_dir)
from modules.mains import log
from modules.mains.suite import Suite

test_dir = base_dir+"/modules/run04"
description = u"run04自动化测试报告"
test_file = "*test.py"


def test_run04():
    suitex = Suite()
    suitex.run_suite(test_dir,test_file,description)


if __name__ == '__main__':   
    test_run04()

#coding=utf-8
from os import path as opath
from sys import path as spath
base_dir=opath.dirname(opath.dirname(opath.realpath(__file__)))
base_dir=base_dir.replace('\\', '/')
spath.append(base_dir)

from modules.mains.log import takin_log
from modules.mains.suite import Suite

test_dir = base_dir+"/modules/run03"
description = u"run03自动化测试报告"
test_file = "*test.py"

@takin_log("run03系统测试")
def test_run03():
    suitey = Suite()
    suitey.run_suite(test_dir,test_file,description)

if __name__ == '__main__':   
    test_run03()

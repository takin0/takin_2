#coding=utf-8
from os import path as opath
from sys import path as spath
base_dir=opath.dirname(opath.dirname(opath.realpath(__file__)))
base_dir=base_dir.replace('\\', '/')
spath.append(base_dir)

from modules.mains.log import takin_log
from modules.mains.suite import Suite

test_dir = base_dir+"/modules/run04"
description = u"run04自动化测试报告"
test_file = "*test.py"

@takin_log("run04系统测试")
def test_run04():
    suitex = Suite()
    suitex.run_suite(test_dir,test_file,description)

if __name__ == '__main__':   
    test_run04()

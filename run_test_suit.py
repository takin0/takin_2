#coding=utf-8
from os import path as opath
from threading import Thread
base_dir=opath.dirname(opath.realpath(__file__))
base_dir=base_dir.replace('\\', '/')

from modules.mains.log import takin_log
from modules import run_run04_test
from modules import run_run03_test

threads = []
t1 = Thread(target=run_run03_test.test_run03)
t2 = Thread(target=run_run04_test.test_run04)

threads.append(t1)
threads.append(t2)
for t in threads:
    t.start()
for t in threads:
    t.join()
    

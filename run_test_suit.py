#coding=utf-8
import sys,os,time
import threading
#import multiprocessing

base_dir=os.path.dirname(os.path.realpath(__file__))
base_dir=base_dir.replace('\\', '/')

from modules.mains import log
from modules import run_run04_test
from modules import run_run03_test
    

  
threads = []

t1 = threading.Thread(target=run_run03_test.test_run03) 
#t2 = threading.Thread(target=run_run04_test.test_run04)

threads.append(t1)
#threads.append(t2)

for t in threads:
    t.start()
    
for t in threads:
    t.join()
    





# -*- coding: utf-8 -*-
import threading

def _init():#初始化
    global _global_dict
    
    #定义线程内对象
    _global_dict = threading.local()

def set_global(key,value):
    """ 定义一个全局变量 """
    #错误的写法 exec("_global_dict.{}={}".format(key，value))
    exec("_global_dict.{}=value".format(key))
    
def get_global(keya,defValue=None):
    try:

        value =  eval("_global_dict.{}".format(keya))
        return value
    except :
        return defValue

    
_init()

#zz =type(_global_dict)
#set_global('name','valuez')
#set_global('psss','1231121')
#zz = get_global('name')
#print(zz)
#print(get_global('psss'))

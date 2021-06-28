#coding=utf-8 
from os import path as opath
from logging.config import fileConfig
from logging import getLogger
import functools
path_base=opath.dirname(opath.dirname(opath.dirname(opath.realpath(__file__))))
path_base=path_base.replace('\\', '/')

fileConfig(path_base+'/conf/logging.conf')
logger = getLogger('file')
#loggerp = logging.getLogger('conslo')

def takin_log(info=""):
    def takins_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                #func(*args, **kwargs)
                return func(*args, **kwargs)
            except Exception as e:
                logger.exception(info)
            #raise
            #return func(*args, **kwargs)
        return wrapper
    return takins_log
    #return func


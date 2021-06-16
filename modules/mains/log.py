#coding=utf-8 
import os,logging
import logging.config
import functools
path_base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base=path_base.replace('\\', '/')

logging.config.fileConfig(path_base+'/conf/logging.conf')
logger = logging.getLogger('file')
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


#coding=utf-8
#截图函数
from os import path as opath,listdir,makedirs
from sys import path as spath
from time import strftime,localtime,time
path_base=opath.dirname(opath.dirname(opath.dirname(opath.realpath(__file__))))
path_base=path_base.replace('\\', '/')
spath.append(path_base)
from modules.mains.log import takin_log

class TestReport():

        @takin_log("创建报告失败")
        def creat_report(self,sign = ''):
                newdir = "Test_" + sign + '_' + strftime('%Y%m%d%H%M%S',localtime(time()))
                file_path=path_base+"/report/"+newdir+"/image/"
                makedirs(file_path)
                report_path=path_base+"/report/"+newdir+"/test.txt"
                file_path = path_base+"/report/"+newdir
                #print(file_name)
                return report_path,file_path,newdir

        @takin_log("获取报告失败")
        def get_newreport(self,parma = ''):
                dir_path=path_base+"/report/"#测试报告路径
                dirlist = listdir(dir_path)
                if parma == 'm':
                        mdirlist = sorted(dirlist, key=lambda x: opath.getmtime(opath.join(dir_path, x)))
                        mnewdir=mdirlist[-1]
                        newdir=mnewdir
                elif parma == 'a':
                        adirlist = sorted(dirlist, key=lambda x: opath.getatime(opath.join(dir_path, x)))
                        anewdir=adirlist[-1]
                        newdir=anewdir
                else:
                        cdirlist = sorted(dirlist, key=lambda x: opath.getctime(opath.join(dir_path, x)))
                        cnewdir=cdirlist[-1]
                        newdir=cnewdir#最新报告文件夹           
                file_path=dir_path+newdir#最新报告文件夹路径
                return file_path,newdir

if __name__=='__main__':
        report=TestReport()
        y = report.creat_report("yancloud")
        print(y)

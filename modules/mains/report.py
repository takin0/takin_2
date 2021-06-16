#coding=utf-8
#截图函数
import os,sys,time,datetime
path_base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base=path_base.replace('\\', '/')
sys.path.append(path_base)
from modules.mains import log

class TestReport():
        #log.logger.info("xxxxxx")
        def creat_report(self,sign = ''):
                newdir = "Test_" + sign + '_' + time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
                file_path=path_base+"/report/"+newdir+"/image/"
                fp=os.makedirs(file_path)
                report_path=path_base+"/report/"+newdir+"/test.txt"
                file_path = path_base+"/report/"+newdir
                #print(file_name)
                return report_path,file_path,newdir

        def get_newreport(self,parma = ''):
                dir_path=path_base+"/report/"#测试报告路径
                dirlist = os.listdir(dir_path)
                if parma == 'm':
                        mdirlist = sorted(dirlist, key=lambda x: os.path.getmtime(os.path.join(dir_path, x)))
                        mnewdir=mdirlist[-1]
                        newdir=mnewdir
                elif parma == 'a':
                        adirlist = sorted(dirlist, key=lambda x: os.path.getatime(os.path.join(dir_path, x)))
                        anewdir=adirlist[-1]
                        newdir=anewdir
                else:
                        cdirlist = sorted(dirlist, key=lambda x: os.path.getctime(os.path.join(dir_path, x)))
                        cnewdir=cdirlist[-1]
                        newdir=cnewdir#最新报告文件夹           
                file_path=dir_path+newdir#最新报告文件夹路径
                return file_path,newdir

if __name__=='__main__':
        report=TestReport()
        y = report.creat_report("yancloud")
        #x=report.get_newreport("a")
        print(y)

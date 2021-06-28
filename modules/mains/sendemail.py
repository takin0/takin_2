#coding=utf-8 
from os import path as opath
from sys import path as spath
from os import walk,remove
from smtplib import SMTP,SMTPException
from zipfile import ZipFile
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from time import sleep

path_base=opath.dirname(opath.dirname(opath.dirname(opath.realpath(__file__))))
path_base=path_base.replace('\\', '/')
spath.append(path_base)
from modules.mains.log import takin_log
from modules.mains.report import TestReport
from modules.mains.load_ini import ReadConfig

report = TestReport()
emlcf = ReadConfig()
email_smtpserver = emlcf.get_emcf("smtpserver")
email_username = emlcf.get_emcf("username")
email_password = emlcf.get_emcf("password")
email_from_addr = emlcf.get_emcf("from_addr")
email_to_addr = emlcf.get_emcf("to_addr")
email_port = emlcf.get_emcf("port")

@takin_log("发送邮件失败")
def send_mail(report_path):
    #source_dir = report.get_newreport()  # 查找最新报告的路径
    #source_path = source_dir[0]#打包报告的路径
    source_path = report_path
    output_filename = source_path+'.zip'#打包后的存放路径
    #打包测试报告
    zipf = ZipFile(output_filename, 'w')
    pre_len = len(opath.dirname(source_path))
    for parent, dirnames, filenames in walk(source_path):
        for filename in filenames:
            pathfile = opath.join(parent, filename)
            arcname = pathfile[pre_len:].strip(opath.sep)   #相对路径
            zipf.write(pathfile, arcname)
    zipf.close()
    #寄件邮箱
    smtpserver = email_smtpserver
    from_addr = email_username
    password = email_password
    port = email_port
    #附件路径及文件名
    #get_report = report.get_newreport()#再次调用查找打包好的文件
    file_name = output_filename.split("/")[-1]#打包后的文件名
    file = output_filename#打包后的路径
    #print(file_name)
    #print(file)
    #邮件主题
    subject = '测试报告'
    #收件人
    to_addr = email_to_addr
    #创建附件实例
    mg = MIMEMultipart()
    mg['Subject'] = subject
    mg['From'] = formataddr(["自动化测试程序",from_addr])
    mg.attach(MIMEText('您好，本次自动化测试已结束，测试报告以附件形式发送，请查阅！', 'plain', 'utf-8'))
    #mg.attach(MIMEText(open(report_path+"/report.html",'rb').read(), 'html','utf-8'))
    fj = MIMEApplication(open(file,'rb').read())
    fj.add_header('Content-Disposition','attachment',filename=file_name)
    mg.attach(fj)

    try:
        smtpObj = SMTP(smtpserver,port,timeout=20)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(from_addr,password)
        sleep(2)
        smtpObj.sendmail(from_addr, to_addr .split(","), mg.as_string())
        sleep(2)
        smtpObj.quit()
        print ("邮件发送%s成功"%email_to_addr)
        remove(file)#将打包的文件删除
    except SMTPException:
        print ("发送邮件失败")

if __name__ == '__main__':
        send_mail("F:\pythonI\takin-master\report\Test_xdata_20210601172418")

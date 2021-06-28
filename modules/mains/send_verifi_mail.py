#coding=utf-8 
from os import path as opath
from sys import path as spath
from smtplib import SMTP
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
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

@takin_log("发送验证码失败")
def send_verifi_mail(img,subject='Verification Code'):
    smtpserver = email_smtpserver
    from_addr = email_username
    password = email_password
    port = email_port
    file = open(img, "rb")
    img_data = file.read()
    file.close()
    #收件人
    to_addr = email_to_addr
    #创建附件实例
    mg = MIMEMultipart()
    mg['Subject'] = subject
    mg['From'] = formataddr(["自动化测试程序",from_addr])
    mg.attach(MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8'))
    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    mg.attach(img)
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
        print ("验证码发送成功")
    except smtplib.SMTPException:
        print ("发送验证码失败")

if __name__ == '__main__':
        send_verifi_mail()

#coding=utf-8 
import os,sys,smtplib,zipfile
from email.utils import formataddr
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from time import sleep

path_base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base=path_base.replace('\\', '/')
sys.path.append(path_base)
from modules.mains import log
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

def send_verifi_mail(img,subject='Verification Code'):
    smtpserver = email_smtpserver
    from_addr = email_username
    password = email_password
    port = email_port
    
    file = open(img, "rb")
    img_data = file.read()
    file.close()
    #邮件主题
    
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
        smtpObj = smtplib.SMTP(smtpserver,port,timeout=20)
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

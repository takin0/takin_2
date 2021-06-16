#! encoding:utf8
import os,sys
path_base=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
path_base=path_base.replace('\\', '/')
sys.path.append(path_base)

import imaplib
import email,time,datetime
from email.header import decode_header
from time import sleep
from modules.mains.load_ini import ReadConfig

emlcf = ReadConfig()

email_popserver = emlcf.get_emcf("popserver")
email_username = emlcf.get_emcf("username")
email_password = emlcf.get_emcf("password")
email_from_addr = emlcf.get_emcf("from_addr")
email_addr = emlcf.get_emcf("to_addr")
email_popport = emlcf.get_emcf("popport")

def parseBody(message):
    """ 解析邮件/信体 """
    # 循环信件中的每一个mime的数据块
    times = 1
    for part in message.walk():
        
        # 这里要判断是否是multipart，是的话，里面的数据是一个message 列表
        if  not part.is_multipart():
            charset = part.get_charset()
            contenttype = part.get_content_type()
            if contenttype == 'text/plain':
                txt=(str(part.get_payload(decode=True),encoding="gbk"))
                qqq = 0
                return txt
        if times != 1:
            break


def get_new_Mail_txt(num):            
    try:
        serv = imaplib.IMAP4_SSL(email_popserver, email_popport)
    except Exception as e:
        serv = imaplib.IMAP4(email_popserver, email_popport) 
    serv.login(email_username, email_password)
    serv.select()
    typ, data = serv.search(None, 'ALL')
    typ, data = serv.fetch(num, 'RFC822')
    text = data[0][1]
    message = email.message_from_string(str(text,encoding="gbk")) # 转换为email.message对象
    txt = parseBody(message)
    serv.store(num, '+FLAGS', '\\Deleted')
    serv.expunge()
    serv.close()
    serv.logout()
    return txt

    
def get_subisverifi_mail():
    T=time.time()
    #subject = 'Your SSL Certificate'
    sub = '未收到验证码!!!!!'
    conn = imaplib.IMAP4_SSL(email_popserver, email_popport)
    conn.login(email_username, email_password)
    conn.select()
    resp, item = conn.search(None,'UNSEEN')
    mail_id=''
    for i in range(0,len(item[0].split())):
        resp,mailData = conn.fetch(item[0].split()[i],'(RFC822)')
        mailText = mailData[0][1]
        msg = email.message_from_bytes(mailText)
        subject = msg['Subject']
        subdecode = decode_header(subject)
        if subdecode[0][1] == None:
            sub = subdecode[0][0]
            #print(subdecode[0][0])
        else:
            #print(subdecode[0][0].decode(subdecode[0][1]))
            sub = subdecode[0][0].decode(subdecode[0][1])
        if "回复：Verification Code" in sub:
            mail_id = item[0].split()[i]
            break
            
    conn.close()
    conn.logout()
    #print(mail_id)
    return sub,mail_id

def get_verifi_mail(n=4,gjz="回复：Verification Code"):
    isloop = True
    times = 1
    while isloop:
        subjects = get_subisverifi_mail()
        subject =subjects[0]
        sleep(2)
        times+=1
        txt = "未收到验证码!!!!!"
        #print(mail_sub)
        if gjz in subject:
            num = subjects[1]
            isloop = False
            txt = get_new_Mail_txt(num)

            #print('txt'+txt)
        elif times > 120:
            isloop = False
    return txt[0:n]

if __name__ == '__main__':
    print(get_verifi_mail())

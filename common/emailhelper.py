#-*- coding: utf-8 -*-
'''
MailHelper is used for sending mail
'''
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import os
 
class MailHelper(object):
  
  @classmethod
  def send_email(cls, subject, content, from_addr, to_addr, nick_name):
    password = '123456abc'
    smtp_server = 'smtp.163.com'
 
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = '[报警] <%s>' % from_addr
    msg['To'] = '%s <%s>' % (nick_name, to_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()
 
    server = smtplib.SMTP(smtp_server, 25, 5)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

MailHelper.send_email(subject='Alert',
    content='this is alert', from_addr='18647246574@163.com',
    to_addr='397283864@qq.com', nick_name='Herry')
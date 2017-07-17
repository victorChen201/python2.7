#!/usr/bin/env python
# coding=utf-8
#========================================== 
# 导入smtplib和MIMEText 
#========================================== 
from email.mime.text import MIMEText 
from email.MIMEBase import MIMEBase
from email import Encoders
import email.mime.multipart
from email.MIMEMultipart import MIMEMultipart
import smtplib 
#========================================== 
# 要发给谁，这里发给3个人 
#========================================== 
mailto_list=["shuangshengchen@qq.com","hongxin_228@163.com"] 
#========================================== 
# 设置服务器，用户名、口令以及邮箱的后缀 
#========================================== 
mail_host="smtp.qq.com"
mail_user="shuangshengchen"
mail_pass="fztzdcapgyhjcbch" #qq要求授权码，密码不行，你要在手机发短信具体的上qq邮箱网站上看
mail_postfix="qq.com"
#========================================== 
# 发送邮件 
#========================================== 
def send_mail(to_list,sub,content): 
    ''''' 
    to_list:发给谁 
    sub:主题 
    content:内容 
    send_mail("xxx@xxxx.com","主题","内容") 
    '''
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEMultipart() #MIMEText(content) 发送文本 
    msg['Subject'] = sub 
    msg['From'] = me 
    msg['To'] = ";".join(to_list)
    #附件内容，若有多个附件，就添加多个part, 如part1，part2，part3
    part = MIMEBase('application', 'octet-stream')
    # 读入文件内容并格式化，此处文件为当前目录下，也可指定目录 例如：open(r'/tmp/123.txt','rb')
    part.set_payload(open('test.txt','rb').read())
    Encoders.encode_base64(part)
    ## 设置附件头
    part.add_header('Content-Disposition', 'attachment; filename="test.txt"')
    msg.attach(part)
    try: 
        s = smtplib.SMTP_SSL(mail_host, 465) 
        s.set_debuglevel(1)
        s.login(mail_user,mail_pass) 
        s.sendmail(me, to_list, msg.as_string()) 
        s.close() 
        return True
    except Exception, e: 
        print str(e) 
        return False

if __name__ == '__main__': 
    if send_mail(mailto_list,"主题","内容"): 
        print "发送成功"
    else: 
        print "发送失败"


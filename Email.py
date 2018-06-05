import smtplib
from email.mime.text import MIMEText
from email.header import Header
import socket
import os
import aliyundns
import requests


def getip():
    rosepse = requests.get("http://myip.dnsomatic.com/")
    return rosepse.text

if __name__ == '__main__':
        
    while 1:
        # 检测是否有网
        exit_code = os.system('ping www.baidu.com')
        if exit_code:
            pass

        else:
            # ip = socket.gethostbyname(socket.gethostname())
            # print(ip)
            ip = getip()
            print('get ip :' + ip )
            msg = MIMEText('IP:'+str(ip), 'plain', 'utf-8')
            aliyundns.update_dns()
            msg['Subject'] = Header("IP地址发送", 'utf-8')
            #报错原因是因为“发件人和收件人参数没有进行定义
            # 发送的邮箱地址
            msg['from'] = '123123@126.com'
            # 接收的邮箱地址
            msg['to'] = 'imqq@qq.com'

            smtp = smtplib.SMTP()
            # smtp服务器
            smtp.connect("smtp.126.com") 
            # 登陆发送账号，密码
            smtp.login("123123@126.com", "123123")
            # 编辑邮件  发送地址/接收地址/内容
            smtp.sendmail("123123@126.com", "imqq@qq.com", msg.as_string())
            smtp.quit()
            print('邮件发送成功email has send out !')
            break




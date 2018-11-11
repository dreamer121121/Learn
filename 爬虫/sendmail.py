from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib


def jiaformatadd(s):  # 输入为字符串
    name, addr = parseaddr(s)
    return formataddr((Header(name,'UTF-8').encode(),addr))


# 发送邮件账号 PS：记得开SMTP
from_addr = '2761564455@qq.com'
# 密码
password = '2119851111'

# 接受邮件账号
to_addr = '2181990549@qq.com'

# 发送服务器
smtup_server = 'smtp.qq.com'

# 邮件内容  MIMEtext中是可以输入html代码的
msg = MIMEText('hi gad with you ')
msg['From'] = jiaformatadd('python邮件测试<%s>'%from_addr)
msg['TO'] = jiaformatadd('管理<%s>'%to_addr)
msg['Subject'] = Header('Test',"UTF-8").encode()

# 发送邮件  一般服务器默认25端口
server = smtplib.SMTP(smtup_server, 25)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()






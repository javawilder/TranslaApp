from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import smtplib
import time
import tkinter
import queue


def send_mail(subject,filename,w):
    email_host = 'smtp.163.com'  # 服务器地址
    sender = '13769299922@163.com'  # 发件人
    password = 'asd876'  # 密码，如果是授权码就填授权码
    receiver = '13769299922@163.com'  # 收件人

    msg = MIMEMultipart()
    msg['Subject'] = subject  # 标题
    msg['From'] = ''  # 发件人昵称
    msg['To'] = ''  # 收件人昵称

    # 正文-图片 只能通过html格式来放图片，所以要注释25，26行
    mail_msg = '''
<p>\n\t 这是电脑自动发送的邮件!</p>
<p>\n\t 不必回复。</p>
<p><a href="https://www.jianshu.com/u/ee5f3fe1b932">简书</a></p>
<p>如遇到问题或发现Bug，请联系：13769299922</p>
<p><img src="cid:image1"></p>
'''
    msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    # 指定图片为当前目录
    # fp = open(r'111.png', 'rb')
    # msgImage = MIMEImage(fp.read())
    # fp.close()
    # # 定义图片 ID，在 HTML 文本中引用
    # msgImage.add_header('Content-ID', '<image1>')
    # msg.attach(msgImage)

    ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    # 附件-图片
    # image = MIMEImage(open(r'111.jpg', 'rb').read(), _subtype=subtype)
    # image.add_header('Content-Disposition', 'attachment', filename='img.jpg')
    # msg.attach(image)
    # 附件-文件
    file = MIMEBase(maintype, subtype)
    file.set_payload(open(filename, 'rb').read())
    file.add_header('Content-Disposition', 'attachment', filename=subject)
    encoders.encode_base64(file)
    msg.attach(file)

    # 发送
    smtp = smtplib.SMTP()
    smtp.connect(email_host, 25)
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    w.Scrolledtext1.insert(tkinter.END,"邮件发送成功至您的邮箱。\r\n")
    w.Scrolledtext1.update()



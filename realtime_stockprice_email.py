# Author: Ru1yi
# Date: 2022-08-29
# Version: 1.0

# smtp is a module that provides an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

#yfinance is a popular open source library developed by Ran Aroussi as a means to access Yahoo Finance API in Python.
#import yfinance as yf

# tushare is a Python package for crawling and analyzing data from China's largest stock exchange market.
import tushare as ts

# 你的邮箱账号
my_sender = 'sender@qq.com' 
# 在邮箱设置中生成的授权码，注意是smtp授权码，不是邮箱密码!!!!!!!!!!
my_pass = ''  
# 接收邮件的邮箱              
my_user = 'user@qq.com' 

# 首先需要进行初始化，设置你的 token，token 为在 tushare 网站注册获得
ts.set_token('your token')

# 初始化 pro 接口
pro = ts.pro_api()

# 例如获取 '600848' 这只股票的实时数据
df = ts.get_realtime_quotes('600848')
user_name = '杨师，'
stock_name = str(df.name[0])+'当前的价格是：'
stock_price = df.price[0]
msg_to_send = user_name+stock_name+stock_price
# print(msg_to_send)

# 监控股票价格
price_threshold = 300

# 电子邮件内容
def mail():
    ret = True
    try:
        msg = MIMEText(msg_to_send,'plain', 'utf-8')
        msg['From'] = formataddr(["Ru1yi", my_sender])  
        msg['To'] = formataddr(["杨师", my_user])  
        msg['Subject'] = "Python邮件测试" 
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 这种写法仅支持qq邮箱，@qq.com @foxmail.com等
        server.login(my_sender, my_pass)  
        server.sendmail(my_sender, [my_user, ], msg.as_string())  
        server.quit()  
    except Exception:  
        ret = False
    return ret

if stock_price > price_threshold:
    ret=mail()
    if ret:
        print("邮件发送成功")    
    else:
        print("邮件发送失败")
    timeout(10)
    


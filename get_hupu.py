import json
import requests
from bs4 import  BeautifulSoup
from datetime import datetime
import  smtplib
from email.mime.text import MIMEText
from email.header import Header
# 取时间为文件名
date = str(datetime.now())[11:13] +'-'+str(datetime.now())[14:16]
# print(date)


try:
    r = requests.get(url='https://bbs.hupu.com/search?q=%E6%9D%9C%E5%85%B0%E7%89%B9&topicId=&sortby=general&page=1')
    ht = r.text
    # f =open('./{}.html'.format(date),'w',encoding='utf-8')
    f = open(f'{date}.html', 'w', encoding='utf-8')
    f.write(ht)
    f.close()

except Exception as e:
    print(e)
# finally:
#     # os.rename('hupu.html',f'hupu{date}.html')
#     print('try done')
fh=open(f'{date}.html','r',encoding='utf-8')  #打开文件，指定模式和编码
soup = BeautifulSoup(fh,'lxml')   #传入文件
# print(soup.prettify())  #格式化
s1=soup.find_all("a",class_="content-wrap-span")
list1=[]
for x in s1:   #遍历搜索结果，取出字段,放进字典再放进列表
    dict1={}
    n = x.get('href')
    dict1[x.text]=n
    # if len(n) > 30:
    list1.append(dict1)
# print(list1[1:])
# print(soup.)
fh.close()
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "457638186@qq.com"  # 用户名
mail_pass = "ksdnbntsyyxxcbbh"  # 口令
from email.mime.multipart import MIMEMultipart
sender = '457638186@qq.com'
receivers = ['457638186@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = json.dumps(list1,ensure_ascii=False)   #json dumps把python对象转换成json字符串，json_load反之
email = MIMEMultipart()
email['From']='457638186@qq.com'
email['To']='john526@foxmai.com'
email['subject'] = Header('Python SMTP 邮件测试','utf-8')
email.attach(MIMEText(message,'plain','utf-8'))

if __name__== '__main__':

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.qq.com',465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, email.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        import traceback

        traceback.print_exc()
        print("无法发送邮件")



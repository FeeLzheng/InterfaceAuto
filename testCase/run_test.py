from email.mime.multipart import MIMEMultipart
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time
import unittest
import os
import sys

from common.Log import MyLog as Log
sys.path.append("C:\\Users\\Administrator\\PycharmProjects\\InterfaceAuto\\testCase\\device\\")
sys.path.append("C:\\Users\\Administrator\\PycharmProjects\\InterfaceAuto\\testCase\\tesFile\\")
sys.path.append("C:\\Users\\Administrator\\PycharmProjects\\InterfaceAuto\\testCase\\")
import readConfig as readConfig
from testCase.device.test import InterFace

log = Log.get_log()
logger = log.get_logger()
localReadConfig =readConfig.readConfig()
on_off=localReadConfig.get_email("on_off")

#==========定义发送邮件=========
def send_mail(new_file):
    print(new_file)
    f = open(new_file,"rb")
    mail_body = f.read()
    f.close()

    msg =MIMEText(mail_body,"html","utf-8")
    # msg["Content-Type"]='application/octet-stream'
    # msg["Content-Disposition"]='attachment,filename="uni-ubi.html"'
    # msgRoot=MIMEMultipart('related')
    # subject="登录界面自动化测试报告"
    # msg["Subject"]=subject
    msg["Subject"]=Header("测试报告","utf-8")
    # msgRoot.attach(msg)
    msg['From'] = localReadConfig.get_email("sender")
    msg['To'] = localReadConfig.get_email("receiver")

    smtp=smtplib.SMTP()
    smtp.connect(localReadConfig.get_email("mail_host"))
    smtp.starttls()
    print("126邮箱登入前")
    smtp.login (localReadConfig.get_email("sender"), localReadConfig.get_email("mail_pass"))
    print("126邮箱登入成功")
    smtp.sendmail(localReadConfig.get_email("sender"),localReadConfig.get_email("receiver"),msg.as_string())
    print("126发送邮件成功")
    smtp.quit()
    print("mail has send out")



#=====================查找测试报告目录，找到最新生产的测试报告文件====================
def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getatime(testreport + "\\" +fn))
    file_new=os.path.join(testreport,lists[-1])
    print(testreport)
    print(file_new)
    return file_new


def run():
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    file_name="../report/"+now+"result.html"
    fp=open(file_name,"wb")
    runner=HTMLTestRunner(stream=fp,title="接口测试",description="")
    discover=unittest.defaultTestLoader.discover("./device/",pattern="testI*.py")
    try:
        runner.run(discover)
    except Exception as ex:
        logger.error(str(ex))
    finally:
        logger.info("*********TEST END*********")
        fp.close()
        file_path = new_report("../report/")
        # send test report by email
        if on_off == 'on':
            send_mail(file_path)
        elif on_off == 'off':
            logger.info("Doesn't send report email to developer.")
        else:
            logger.info("Unknow state.")



if __name__=="__main__":
    run()


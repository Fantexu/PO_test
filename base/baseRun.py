import os
import smtplib
import time
import unittest
import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def add_case(case_path, rule='test*.py'):

    suite = unittest.TestSuite()
    discover = unittest.TestLoader().discover(case_path, rule)
    suite.addTests(discover)
    return suite


def run_case(suite):
    unittest.TextTestRunner().run(suite)


def run_case_HTMLText(suite, report_path):
    report = os.path.join(report_path, '{}_report.html'.format(time.strftime('%Y%m%d_%H_%M_%S')))
    with open(report, 'wb') as file:
        runner = HTMLTestRunner.HTMLTestRunner(file, title='测试报告', description='用例执行情况')
        runner.run(suite)


def get_report(report_path):
    report_list = os.listdir(report_path)
    report_list.sort(key=lambda report: os.path.getmtime(os.path.join(report_path, report)))
    return os.path.join(report_path, report_list[-1])


def send_main(report_path, sender, pwd, recevier, server, port=0):
    with open(get_report(report_path), 'rb') as file:
        mail_body = file.read()

    msg = MIMEMultipart()
    msg['Subject'] = '{}_用例报告'.format(time.strftime('%Y_%m_%d %H_%M_%S'))
    msg['from'] = sender
    msg['to'] = ';'.join(recevier)

    body = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(body)

    # 上传附件
    accessory = MIMEText(mail_body, 'base64', 'utf-8')
    accessory['Content-Type'] = 'application/octet-stream'
    accessory['Content-Disposition'] = 'attachment; filename= "result.html"'
    msg.attach(accessory)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(server)
    except:
        smtp = smtplib.SMTP_SSL(server, port)

    smtp.login(sender, pwd)
    smtp.sendmail(sender, recevier, msg.as_string())
    smtp.quit()
    print('邮件发送成功')


if __name__ == '__main__':
    print(os.getcwd())
    a = os.path.join(os.getcwd(), '..')
    print(a)

import yagmail
import yaml
from utils.config import Config, REPORT_PATH


class SendMail(object):

    def __init__(self):
        mailcfg = Config().get('mailCfg')
        self.uname = mailcfg['user']
        self.pwd = mailcfg['password']
        self.smtp = mailcfg['smtp']
        self.to = mailcfg['revivers']
        self.subject = mailcfg['subject']
        self.content = mailcfg['content']

    def send_mail(self, attachment=None):
        yag = yagmail.SMTP(host=self.smtp, user=self.uname, password=self.pwd)
        try:
            yag.send(to=self.to, subject=self.subject, contents=self.content, attachments=attachment)
            print("Succeed")
            return True
        except yagmail.YagAddressError:
            print("Failed")
            return False


if __name__ == '__main__':
    mail = SendMail()
    mail.send_mail(REPORT_PATH + '/测试报告.html')
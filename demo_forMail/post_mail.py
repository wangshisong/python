# coding = utf-8

import os
from django.core.mail import send_mail,EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'project1.settings'

if __name__ == '__main__':
    send_mail(
        '这是邮件的标题',
        '这是邮件的内容！',
        'qq704496591@sina.com',
        ['qq704496591@sina.com'],
    )

# coding = utf-8

from django.urls import path
from app01_method.views import *

app_name = 'app01_method'
urlpatterns = [
    path('login_logic/', login_logic, name='login_logic'),                  # 登陆函数
    path('register_logic/', register_logic, name='register_logic'),         # 注册函数
    path('codes/', codes, name='codes'),                                    # 验证码
    path('checkName/', checkName, name='checkName'),                        # 命名判断
    path('check/', check, name='check'),                                    # 验证码ajax
    path('send_email/', send_email, name='send_email'),                     # 发送邮件
    path('send_emaill/', send_emaill, name='send_emaill'),                  # 邮件判断
]

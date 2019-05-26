import hashlib
import re

from django.contrib.auth.hashers import make_password,check_password
from django.core.mail import EmailMultiAlternatives

from captcha.image import ImageCaptcha
import random, string
from app01.views import *
# Create your views here.


# 登陆函数
from project1 import settings


def login_logic(request):
    uanme = request.POST.get('txtUsername')  # 邮箱vc z
    password = request.POST.get('txtPassword')  # 密码
    user = TUser.objects.filter(user_email=uanme)[0] # 判断数据库是否存在用户名和密码
    user1 = check_password(password,user.user_password)
    number = str(request.POST.get('number')).lower()
    code = str(request.session.get('code')).lower()
    if user and user1 and code == number:
        res = redirect('app01:index')
        # 数据库存储session，登录状态
        print(user.user_name,18)
        request.session['login'] = user.user_name
        return res
    return redirect("app01:login")


# 注册函数
def register_logic(request):
    phone = request.POST.get('txt_username')                                        # 获取邮箱号
    upwd = request.POST.get('txt_password')                                         # 获取密码
    password = make_password(upwd)                                                  # 加密密码
    uanme = request.POST.get('txt_name')
    number = str(request.POST.get('txt_vcode')).lower()
    code = str(request.session.get('code')).lower()
    if number == code:
        res = redirect('app01:register_ok')
        TUser.objects.create(user_email=phone, user_password=password, user_name=uanme, password=upwd)  # 邮箱和密码存数据库库
        res.set_cookie('username', phone, max_age=7 * 60 * 24 * 60)
        send_email(phone, code)
        return res  # 返回成功页面
    elif phone == '' or password == '' or number != code:                            # 判断邮箱为空或者密码为空
        return redirect('app01:register')                                            # 返回注册
# -------------------------------------------------------------------------------------------


# 邮件发送
def send_email(email, code):
    email1 = TUser.objects.filter(user_email=email)[0]
    Postbox.objects.create(postbox_name=email1.id, code=code)
    subject = 'python157'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/?code={}" target=blank>www.baidu.com</a>，\欢迎你来验证你的邮箱，验证结束你就可以登录了！</p>'.format('127.0.0.1:8000/app01/app01_method/send_emaill', code)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


# 邮件判断
def send_emaill(request):
    code = request.GET.get('code')
    sende = Postbox.objects.filter(code=code)
    if sende:
        send_id = sende[0].postbox_name
        print(send_id,68)
        sendem = TUser.objects.filter(id=send_id)
        print(sendem,70)
        ss = sendem[0]
        ss.user_status = 1
        ss.save()
        uanme = sendem[0].user_name
        request.session['login'] = uanme
        return HttpResponse('注册成功')
    return HttpResponse('注册失败')


# ----------------------------------------------------------------------------------------
# 验证码
def codes(request):
    image = ImageCaptcha()  # 构造一个image对象
    code = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 4)
    code = "".join(code)
    request.session['code'] = code
    print(code, '----------------')
    data = image.generate(code)
    re = request.session.get("code")
    return HttpResponse(data, "image/png")


# 命名判断
def checkName(request):
    username = request.POST.get("username")
    re_name = re.findall(
        '\w+@[0-9a-zA-Z]{2,3}\.com|^138\d{8}$|^159\d{8}$|^136\d{8}$|^171\d{8}$|^177\d{8}$|^149\d{8}$|^183\d{8}$',
        username)
    print(username)
    if username == '':
        return HttpResponse('null')
    request = TUser.objects.filter(user_email=username)
    print(request)
    if request:
        return HttpResponse('已存在')
    elif not re_name:
        return HttpResponse('格式不正确')
    else:
        return HttpResponse('用户名合法')


# 验证码ajax
def check(request):
    number = request.GET.get('username')
    code = request.session.get('code')
    print(number,80)
    print(code,81)
    if number == '':
        return HttpResponse("验证码不能为空")
    if code.lower() == number.lower():
        return HttpResponse("验证码正确")  # 只需要返回部分内容，不需要返回整个html文件
    return HttpResponse("验证码错误")

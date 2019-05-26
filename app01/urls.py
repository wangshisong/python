# coding = utf-8
from django.urls import path, include
from app01.views import *


app_name = 'app01'
urlpatterns = [
    path('index/', index, name="index"),
    path('detail/', detail, name='detail'),
    path('booklist/', booklist, name='booklist'),
    path('car/', car, name='car'),
    path('indent/', indent, name='indent'),
    path('indent_ok/', indent_ok, name='indent_ok'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('register_ok/', register_ok, name='register_ok'),
    path('del_indexsession/', del_indexsession, name='del_indexsession'),
    path('app01_method/', include('app01_method.urls')),
]

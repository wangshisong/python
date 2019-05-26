# coding = utf-8

from django.urls import path
from shopapp.views import *

app_name = 'shopapp'
urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('del_book/', del_book, name='del_book'),
    path('modify_book/', modify_book, name='modify_book'),
    path('create_order/', create_order, name='create_order'),
]

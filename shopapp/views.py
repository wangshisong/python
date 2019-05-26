from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01.models import *
from cart import Cart
# Create your views here.


def add_book(request):
    bookid = int(request.GET.get('bookid'))
    num = int(request.GET.get('num'))
    print(bookid,'第10行',num)
    if not num:
        num = 1
    print(num)
    cart = request.session.get('cart')
    if cart == None:
        cart = Cart()
        cart.add_book_toCart(bookid,num)
        request.session['cart'] = cart
    else:
        cart.add_book_toCart(bookid,num)
        request.session['cart'] = cart
    print(cart)
    return HttpResponse(1)


def del_book(request):
    bookid = request.GET.get('id')
    cart = request.session.get('cart')
    cart1 = cart.cartltem
    print(cart1,'views,25')
    cart.delete_book(bookid)
    request.session['cart'] = cart
    print(cart1,'views,29')
    return redirect("app01:car")


def modify_book(request):
    bookid = int(request.GET.get('bookid'))
    num = int(request.GET.get('num'))
    cart = request.session.get('cart')
    cart.modify_cart(bookid,num)
    request.session['cart'] = cart
    return HttpResponse(2)


def create_order(request):
    uname = request.POST.get('ship_man')
    request.session['uname'] = uname
    address = request.POST.get('ship_man1')
    zipcode = request.POST.get('ship_man2')
    phone = request.POST.get('ship_man3')
    tel_phone = request.POST.get('ship_man4')
    if TAddress.objects.filter(name=uname,detail_address=address,zipcode=zipcode,phone=phone, tel_phone=tel_phone):
        print('全部显示')
        return redirect('app01:indent_ok')
    elif TAddress.objects.filter(name=uname,detail_address=address,zipcode=zipcode,phone=None, tel_phone=tel_phone):
        print('条件判断，电话null')
        return redirect('app01:indent_ok')
    elif TAddress.objects.filter(name=uname,detail_address=address,zipcode=zipcode,phone=phone, tel_phone=None):
        print('条件判断，固定null')
        return redirect('app01:indent_ok')
    else:
        # 注册新的
        if phone and not tel_phone:
            print('有电话没固定')
            TAddress.objects.create(name=uname, detail_address=address, zipcode=zipcode, phone=phone, tel_phone=None)
            return redirect('app01:indent_ok')
        elif tel_phone and not phone:
            print('有固定没电话')
            TAddress.objects.create(name=uname, detail_address=address, zipcode=zipcode, phone=None, tel_phone=tel_phone)
            return redirect('app01:indent_ok')
        elif phone and tel_phone:
            print('都有需注册')
            TAddress.objects.create(name=uname, detail_address=address, zipcode=zipcode, phone=phone, tel_phone=tel_phone)
            return redirect('app01:indent_ok')
        else:
            return redirect('app01:indent')

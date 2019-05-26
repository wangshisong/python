from django.shortcuts import render, HttpResponse,redirect
from app01.models import *
from django.core.paginator import Paginator

# Create your views here.

couns = 0
numid = []
def index(request):
    cc1 = DCategory.objects.filter(category_pid__isnull=True)
    cc2 = DCategory.objects.filter(category_pid__isnull=False)
    book1 = TBook.objects.all()
    try:
        uname = request.session['login']
        if uname:
            return render(request, 'index1.html', {"re": cc1, "re2": cc2, "re3": book1, 'uname': uname})
    except:
        return render(request, 'index1.html', {"re": cc1, "re2": cc2, "re3": book1})


def del_indexsession(request):
    del request.session['login']
    return redirect('app01:index')


def detail(request):
    id = request.GET.get("id")
    cc = TBook.objects.filter(id=id)
    try:
        uname = request.session['login']
        if uname:
            return render(request, 'Book details.html', {'re': cc, 'uname': uname})
    except:
        return render(request, 'Book details.html', {'re': cc})


def booklist(request):
    global couns,numid
    cc1 = DCategory.objects.filter(category_pid__isnull=True)
    cc2 = DCategory.objects.filter(category_pid__isnull=False)
    number = int(request.GET.get("number"))
    id = request.GET.get('id')
    cid = request.GET.get('cid')
    # 判断页面页数
    if not number:
        number = 1
    if not id:
        id = 1
    if not cid:
        cid = 'book'
    # 判断一级二级分类
    if id not in numid and cid not in numid:
        number = 1
        couns += 1
        numid.append(id)
        numid.append(cid)
    # 判断id是否一致
    if DCategory.objects.filter(id=id):
        if couns % 2 == 0:
            number = 1
            numid = []
        if cid != 'book':
            book1 = TBook.objects.filter(book_category=id, book_category_gory=cid)
        else:
            book1 = TBook.objects.filter(book_category=id)

    user = book1.count()
    cc = int(user / 3)
    if user / 3 > cc:
        cc += 1
        if number > cc:
            number = 1
    pagtor = Paginator(book1, per_page=3)
    page = pagtor.page(number)
    try:
        uname = request.session['login']
        if uname:
            return render(request, 'booklist.html',
                {"re": cc1, "re2": cc2, "re3": page, 'num': cc, 'numbe': user, 'id': id, 'cid': cid, 'uname': uname})
    except:
        return render(request, 'booklist.html',
                      {"re": cc1, "re2": cc2, "re3": page, 'num': cc, 'numbe': user, 'id': id, 'cid': cid})


def car(request):
    num1 = []
    cart = request.session.get('cart')
    if cart:
        save_price = cart.save_price
        total_price = cart.total_price
        cc = cart.cartltem
        for i in cc:
            if i.book.id not in num1:
                num1.append(i.book.id)
        num1 = len(num1)
        try:
            uname = request.session['login']
            if uname:
                return render(request, 'car.html', {'re': cc, 'save_price': save_price, 'total_price': total_price, 'num': num1, 'uname': uname})
        except:
            return render(request, 'car.html', {'re': cc, 'save_price': save_price, 'total_price': total_price, 'num': num1})
    return render(request, 'car.html')


def indent(request):
    cart = request.session.get('cart')
    if cart:
        try:
            total_price = cart.total_price
            cc = cart.cartltem
            uname = request.session['login']
            address = TAddress.objects.all()
            if uname:
                return render(request, 'indent.html', {'re': cc, 'total_price': total_price, 'uname': uname, 'address': address})
        except:
            return render(request, 'indent.html')
    else:
        return redirect('app01:car')


def indent_ok(request):
    cart = request.session.get('cart')
    if cart:
        try:
            cc = cart.cartltem
            uname = request.session['login']
            shou = request.session['uname']
            total_price = cart.total_price
            if shou:
                del request.session['cart']
                return render(request, 'indent ok.html', {'re': cc, 'uname': uname, 'shou': shou, 'total_price': total_price})
        except:
            return render(request, 'indent.html')
    else:
        return redirect('app01:login')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def register_ok(request):
    phone = request.COOKIES.get('username')
    print(phone)
    return render(request, 'register ok.html', {'phone': phone})

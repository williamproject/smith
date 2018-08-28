from django.shortcuts import render, redirect
from myApp.models import *
from django.contrib.auth import authenticate
from django.contrib import auth
def reg(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')
        if pwd != cpwd:
            return redirect('/shopMsg/reg/')
        user = User.objects.create_user(username=username, password=pwd, pwd=cpwd, email=email)
        user.save()
        return render(request, 'login.html')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        log_name = request.POST.get('username')
        log_pwd = request.POST.get('pwd')
        user = authenticate(username=log_name, password=log_pwd)
        if user is not None:
            auth.login(request, user)
            return render(request, 'user_center_info.html', locals())
        else:
            return redirect('/shopMsg/login/')
    else:
        # request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        return render(request, 'login.html')
# 用户中心
def user_info(request):
    return render(request, 'user_center_info.html')
# 订单
def user_order(request):
    user_id = request.GET.get('id')
    user = User.objects.get(id=user_id)
    return render(request, 'user_center_order.html', locals())
# 收货地址
def user_site(request):
    if request.method == "GET":
        user_id = request.GET.get('id')
        user = User.objects.get(id=user_id)
        consignee = Consignee.objects.order_by("-id")[0]
        return render(request, 'user_center_site.html', locals())
    else:
        consignee = request.POST.get('consignee')
        user_id = request.POST.get('user_id')
        detail_add = request.POST.get('address')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        consignees = Consignee.objects.create(consignee=consignee, detail_add=detail_add, phone=phone, postcode=postcode, user_id=user_id)
        return render(request, 'user_center_site.html', locals())
# 购物车
def cart(request):
    user_id = request.GET.get('id')
    user = User.objects.get(id=user_id)
    return render(request, 'cart.html', locals())
# 首页
def index(request):
    shop_type = ShopType.objects.all()
    return render(request, 'index.html', locals())
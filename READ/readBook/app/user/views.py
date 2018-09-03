import os
import uuid

from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from user.forms import UserForm
import json

from user.models import UserRead
from app.valid.valid_field import valid_required


def regist(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        # 验证form中的必填项是否满足条件
        if form.is_valid():
            user = form.save()
            request.session['login_user'] = json.dumps({
                'id': user.id,
                'nickName': user.nickName,
                'icon': user.icon,
            })
            return redirect('index/')

        errors = json.loads(form.errors.as_json())
        print(form.errors)
    return render(request, 'user/regist.html', locals())


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        fielName = str(uuid.uuid4()).replace('-', '')+os.path.splitext(photo.name)[-1]
        filePath = os.path.join(settings.MEDIA_ROOT, fielName)
        print("2222222222222222222",filePath)
        with open(filePath, "wb") as f:
            for chuck in photo.chunks():
                f.write(chuck)
        return JsonResponse({'code': 200, 'path':fielName})
    return JsonResponse({'code': 101, 'msg': '仅支持ＰＯＳＴ'})

def login(request):
    if request.method == 'POST':
        errors = {}
        nickName = request.POST.get('nickName')
        password = request.POST.get('password')
        valid_required('name', '用户', 'nickName', errors)
        valid_required('pwd', '密码', 'password', errors)
        if not errors:
            users = UserRead.objects.filter(nickName=nickName)
            if users.count() > 0:
                user = users[0]
                if check_password(user.password, password):
                    return redirect('index/',locals())
                else:
                    errors['pwd'] = '%s密码输入不正确'%password
                    return render(request, 'user/login.html')
            else:
                errors['name'] = "%s用户不存在"%nickName
                return render(request, 'user/login.html')

    return render(request,'user/login.html', locals())

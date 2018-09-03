import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from myApp.models import Novels
from valid import rank, r


def show(request, art_id):
    art = Novels.objects.get(pk=art_id)

    rank.week_rank(art_id)

    rank_arts = [Novels.objects.get(pk=id) for id in rank.get_art(3)]

    return render(request,'art/show.html',locals())

def buyState(request,id):
    msg = None
    if 'login_user' not in request.session:
        msg= {'code':101,'msg': '请登录'}
    else:
        uid = json.loads(request.session.get('login_user')).id
        if r.hexists('qbuy', uid):
            msg = {
                'code':200,
                'msg':"抢购成功",
                'gid':r.hegt('qbuy',uid).decode()
            }
        else:
            # 判断　抢购数量是否达到上线
            if r.hlen('qbuy')< 5:
                #没有达到上线
                msg = {'code':201,'msg':'抢购中'}
            else:
                msg = {'code':201,'msg':'抢购失败'}
    return JsonResponse(msg)
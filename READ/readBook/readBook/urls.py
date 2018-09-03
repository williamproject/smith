
from django.conf.urls import url, include
from django.core.paginator import Paginator
from django.shortcuts import render
from django.conf.urls.static import static
import xadmin as admin
from myApp.models import Category, Novels, Tag
from django.conf import settings
import json


def index(request):
    cates = Category.objects.filter(parent=None).all()
    p_cate = request.GET.get('p_cate', '')
    if p_cate:
        p_cate = int(p_cate)
        novels = Novels.objects.filter(category__parent_id=p_cate).all()
    else:
        novels = Novels.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(novels, 5)
    novels_page = paginator.page(int(page))
    if "login_user" in request.session:
        login_user = json.loads(request.session.get('login_user'))
    return render(request, 'index.html', locals())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^art/', include('myApp.urls')),
    url(r'^index/', index)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

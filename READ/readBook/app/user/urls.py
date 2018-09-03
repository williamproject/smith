from django.conf.urls import url


from user.views import regist, upload, login

urlpatterns = [
    url(r'^regist/', regist),
    url(r'^upload/', upload),
    url(r'^login/', login)
]
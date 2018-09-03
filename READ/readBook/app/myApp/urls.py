from django.conf.urls import url

from myApp.views import show

urlpatterns = [
    url(r'^show/(\d+)/', show),

]
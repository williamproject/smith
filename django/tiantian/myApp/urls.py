from django.urls import path
from myApp.views import *
app_name = 'myApp'
urlpatterns = [
    path('index/', index, name='index'),
    path('reg/', reg, name='reg'),
    path('login/', login, name='login'),
    path('info/', user_info, name='info'),
    path('order/', user_order, name='order'),
    path('site/', user_site, name='site'),
    path('cart/', cart, name='cart'),
]
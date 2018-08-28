from django.contrib import admin
from myApp.models import *
admin.site.register([User, Consignee, ShopType, Goods])
